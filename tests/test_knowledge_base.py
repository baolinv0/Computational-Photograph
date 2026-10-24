"""Behavioral tests using real, isolated repositories and the public CLI."""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "knowledge_base.py"
CANONICAL = "https://github.com/baolinv0/Computational-Photograph/blob/main/"


class KnowledgeBaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.item = {
            "id": "arxiv-2401.12345",
            "title": "A paper",
            "aliases": ["AP"],
            "kind": "paper",
            "topic": "HDR",
            "source": "https://arxiv.org/abs/2401.12345v2",
            "source_version": "arXiv v2, author description",
            "checked_on": "2026-10-24",
            "first_covered": "2026-10-01",
            "earliest_public_verified": None,
            "verification_scope": "selected methods only; experiments pending",
            "canonical_url": CANONICAL + "papers/arxiv-2401.12345.md",
        }
        self.registry = {"updated_on": "2026-10-24", "items": [self.item]}
        self.write("papers/arxiv-2401.12345.md", "# A paper\n")
        self.save_registry()

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def save_registry(self):
        self.write("archive/registry.json", json.dumps(self.registry))

    def run_cli(self, command):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), command, "--root", str(self.root)],
            capture_output=True, text=True, check=False,
        )
        self.assertNotIn("Traceback", result.stdout + result.stderr)
        return result

    def make_index(self):
        result = self.run_cli("index")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return (self.root / "papers/README.md").read_text(encoding="utf-8")

    def assert_check_error(self, message):
        result = self.run_cli("check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(message, result.stdout)
        return result

    def test_valid_check_is_read_only(self):
        self.make_index()
        before = {p.relative_to(self.root): p.read_bytes()
                  for p in self.root.rglob("*") if p.is_file()}
        result = self.run_cli("check")
        self.assertEqual(result.returncode, 0, result.stdout)
        after = {p.relative_to(self.root): p.read_bytes()
                 for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_duplicate_identity_and_canonical_are_errors(self):
        self.registry["items"].append(copy.deepcopy(self.item))
        self.save_registry()
        result = self.assert_check_error("duplicate id")
        self.assertIn("duplicate canonical_url", result.stdout)

    def test_missing_card_and_orphan_have_path_context(self):
        (self.root / "papers/arxiv-2401.12345.md").unlink()
        self.write("papers/orphan.md", "# Not registered\n")
        result = self.assert_check_error("papers/arxiv-2401.12345.md")
        self.assertIn("missing", result.stdout)
        self.assertIn("papers/orphan.md", result.stdout)
        self.assertIn("no registry entry", result.stdout)

    def test_paper_canonical_must_point_to_its_own_local_card(self):
        self.item["canonical_url"] = CANONICAL + "papers/wrong.md"
        self.save_registry()
        self.assert_check_error("canonical_url")

    def test_external_industry_signal_is_valid_and_excluded_from_index(self):
        industry = copy.deepcopy(self.item)
        industry.update(id="product-camera", kind="industry_signal", title="Camera signal",
                        source="https://example.com/camera", source_version=None,
                        canonical_url="https://github.com/baolinv0/CameraPaper/blob/main/raw/camera.md")
        self.registry["items"].append(industry)
        self.save_registry()
        index = self.make_index()
        self.assertNotIn("Camera signal", index)
        self.assertEqual(self.run_cli("check").returncode, 0)

    def test_corrupted_json_reports_error_without_traceback(self):
        self.write("archive/registry.json", "{broken")
        self.assert_check_error("archive/registry.json")

    def test_invalid_unicode_is_reported_without_replacing_existing_index(self):
        self.make_index()
        original_registry = copy.deepcopy(self.registry)
        original_index = (self.root / "papers/README.md").read_bytes()
        for field in ("title", "id", "key"):
            with self.subTest(field=field):
                self.registry = copy.deepcopy(original_registry)
                if field == "key":
                    self.registry["bad\ud800key"] = "value"
                else:
                    self.registry["items"][0][field] = "bad\ud800value"
                self.save_registry()
                result = self.run_cli("index")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Unicode", result.stdout)
                self.assertEqual((self.root / "papers/README.md").read_bytes(), original_index)
                self.assert_check_error("Unicode")

    def test_invalid_registry_shapes_and_required_values_are_reported(self):
        for value in ([], {"items": {}}, {"items": [None]},
                      {"items": [{"id": "only-an-id"}]},
                      {"items": [dict(self.item, aliases="not a list")]},
                      {"items": [dict(self.item, id=["not a string"])]}):
            with self.subTest(value=value):
                self.registry = value
                self.save_registry()
                self.assert_check_error("archive/registry.json")

    def test_bad_arxiv_identity_and_real_calendar_dates_are_errors(self):
        self.item["source"] = "https://www.alphaxiv.org/abs/2401.99999v1"
        self.item["checked_on"] = "2026-02-30"
        self.item["events"] = [{"date": "yesterday"}]
        self.save_registry()
        result = self.assert_check_error("source identity")
        self.assertIn("checked_on", result.stdout)
        self.assertIn("events[0].date", result.stdout)

    def test_author_pdf_and_null_version_do_not_invent_source_requirements(self):
        self.item["source"] = "https://people.example.edu/author/paper.pdf"
        self.item["source_version"] = None
        self.save_registry()
        self.make_index()
        self.assertEqual(self.run_cli("check").returncode, 0)

    def test_null_checked_on_is_unknown_and_sorts_after_known_dates(self):
        unknown = copy.deepcopy(self.item)
        unknown.update(id="arxiv-2301.12345", title="Unknown check date", checked_on=None,
                       source="https://arxiv.org/abs/2301.12345",
                       canonical_url=CANONICAL + "papers/arxiv-2301.12345.md")
        self.registry["items"].insert(0, unknown)
        self.write("papers/arxiv-2301.12345.md", "# Unknown check date\n")
        self.save_registry()
        index = self.make_index()
        self.assertLess(index.index("[A paper]"), index.index("[Unknown check date]"))
        unknown_row = next(line for line in index.splitlines() if "[Unknown check date]" in line)
        self.assertIn("|  | selected methods only; experiments pending |", unknown_row)
        self.assertEqual(self.run_cli("check").returncode, 0)

    def test_relative_encoded_links_and_fragments_resolve_and_code_is_exempt(self):
        self.write("docs/space name.md", "# A heading\n")
        self.write("docs/has(parens).md", "# Parentheses\n")
        self.write("docs/guide.md", "[up](../papers/arxiv-2401.12345.md#not-validated)\n"
                   '[encoded](space%20name.md "Optional title")\n'
                   "[paren](has(parens).md)\n"
                   "[anchor](#missing-anchor) [web](https://example.com/a)\n"
                   "[mail](mailto:reader@example.com) [site](//example.com)\n"
                   "```markdown\n[template](missing.md) literal \\n\n```\n"
                   "~~~md\n[template](also-missing.md)\n~~~\n"
                   "`[example](inline-missing.md)` and `literal \\n`\n")
        self.write("skills/template.md", "[excluded](missing.md) literal \\n\n")
        self.write(".git/template.md", "[excluded](missing.md)\n")
        self.make_index()
        self.assertEqual(self.run_cli("check").returncode, 0)
        self.write("docs/broken.md", "[broken](not%20here.md#heading)\n")
        self.assert_check_error("docs/broken.md:1")

    def test_literal_backslash_n_in_prose_is_flagged_for_one_or_many_slashes(self):
        self.make_index()
        for slashes in ("\\", "\\\\", "\\\\\\"):
            with self.subTest(slashes=slashes):
                self.write("README.md", "# Title\nText" + slashes + "nAccidental paragraph\n")
                self.assert_check_error("README.md:2")

    def test_latex_math_is_exempt_from_literal_backslash_n_check(self):
        self.make_index()
        self.write("README.md", r"Inline $\nabla f \neq \nu$ and \(\nu\)." + "\n"
                   + "$$\n" + r"\nabla f = \nu" + "\n$$\n"
                   + "\\[\n" + r"\nu \neq 0" + "\n\\]\n")
        self.assertEqual(self.run_cli("check").returncode, 0)
        with (self.root / "README.md").open("a") as output:
            output.write("Outside math \\nAccidental paragraph\n")
        self.assert_check_error("literal backslash-n")

    def test_multiline_inline_link_targets_are_checked(self):
        self.make_index()
        self.write("README.md", "[card](\npapers/arxiv-2401.12345.md\n)\n")
        self.assertEqual(self.run_cli("check").returncode, 0)
        self.write("README.md", "[missing](\npapers/not-here.md\n)\n")
        self.assert_check_error("README.md:1")

    def test_missing_and_stale_index_fail_without_rewriting(self):
        self.assert_check_error("papers/README.md")
        self.make_index()
        self.write("papers/README.md", "# Manual stale contents\n")
        self.assert_check_error("stale")
        self.assertEqual((self.root / "papers/README.md").read_text(), "# Manual stale contents\n")

    def test_index_comparison_detects_changed_line_endings(self):
        index = self.make_index()
        (self.root / "papers/README.md").write_bytes(index.replace("\n", "\r\n").encode())
        self.assert_check_error("stale")

    def test_index_is_complete_sorted_deterministic_and_escapes_cells(self):
        older = copy.deepcopy(self.item)
        older.update(id="arxiv-2301.12345", title="Older paper", checked_on="2026-10-23",
                     source="https://arxiv.org/abs/2301.12345",
                     canonical_url=CANONICAL + "papers/arxiv-2301.12345.md")
        same_day = copy.deepcopy(self.item)
        same_day.update(id="arxiv-2401.00001", title="First today",
                        source="https://arxiv.org/abs/2401.00001",
                        canonical_url=CANONICAL + "papers/arxiv-2401.00001.md")
        self.item.update(title="Title | separated\nsecond line", aliases=["A|B", "two\nlines"],
                         verification_scope="abstract | only\nno replication")
        self.registry["items"] = [older, self.item, same_day]
        for item in (older, same_day):
            self.write("papers/" + item["id"] + ".md", "# Card\n")
        self.save_registry()
        index = self.make_index()
        self.assertIn("Total papers: **3**", index)
        self.assertLess(index.index("First today"), index.index("[Title "))
        self.assertLess(index.index("[Title "), index.index("Older paper"))
        self.assertIn("Title \\| separated<br>second line", index)
        self.assertIn("A\\|B", index)
        self.assertIn("abstract \\| only<br>no replication", index)
        for item in self.registry["items"]:
            self.assertEqual(index.count("](" + item["id"] + ".md)"), 1)
        self.registry["items"].reverse()
        self.save_registry()
        self.assertEqual(self.make_index(), index)
        self.assertEqual(self.run_cli("check").returncode, 0)


if __name__ == "__main__":
    unittest.main()
