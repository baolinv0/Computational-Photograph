#!/usr/bin/env python3
"""Build the registry-based paper index and check local archive integrity offline.

Only inline Markdown links are checked; URL reachability and heading fragments
are outside this tool's scope. Code examples and delimited math are ignored.
"""

import argparse
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


REGISTRY = "archive/registry.json"
INDEX = "papers/README.md"
GITHUB_PATH = "/baolinv0/Computational-Photograph/blob/main/"
REQUIRED = ("id", "title", "kind", "topic", "source", "source_version",
            "checked_on", "verification_scope", "canonical_url")
DATE_FIELDS = {"date", "brief", "earliest_public_verified", "first_covered"}
LINK = re.compile(
    r"!?\[(?:\\.|[^\]\\])*\]\(\s*"
    r"(?:<(?P<angle>[^>\n]+)>|(?P<plain>(?:\\.|[^\s()]|\([^()\s]*\))+))"
    r"(?:\s+[\"'][^\n]*?[\"'])?\s*\)"
)


def parsed_url(value):
    try:
        return urlsplit(value)
    except ValueError:
        return None


def date_issues(value, context):
    issues = []
    if isinstance(value, dict):
        for key, child in value.items():
            location = f"{context}.{key}"
            if child is not None and (key in DATE_FIELDS or key.endswith("_on")):
                try:
                    if not isinstance(child, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", child):
                        raise ValueError
                    date.fromisoformat(child)
                except ValueError:
                    issues.append(f"{location}: invalid date (expected YYYY-MM-DD)")
            issues.extend(date_issues(child, location))
    elif isinstance(value, list):
        for number, child in enumerate(value):
            issues.extend(date_issues(child, f"{context}[{number}]"))
    return issues


def unicode_issues(value, context):
    """Reject JSON's lone surrogates before paths, rendering, or diagnostics."""
    issues = []
    if isinstance(value, str) and re.search(r"[\ud800-\udfff]", value):
        issues.append(f"{context}: invalid Unicode surrogate codepoint")
    elif isinstance(value, dict):
        for key, child in value.items():
            location = f"{context}[{json.dumps(key, ensure_ascii=True)}]"
            issues.extend(unicode_issues(key, location))
            issues.extend(unicode_issues(child, location))
    elif isinstance(value, list):
        for number, child in enumerate(value):
            issues.extend(unicode_issues(child, f"{context}[{number}]"))
    return issues


def load_registry(root):
    try:
        registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as error:
        return None, [f"{REGISTRY}: cannot read valid JSON: {error}"]
    invalid_unicode = unicode_issues(registry, REGISTRY)
    if invalid_unicode:
        return None, invalid_unicode
    if not isinstance(registry, dict):
        return None, [f"{REGISTRY}: root must be an object"]
    if not isinstance(registry.get("items"), list):
        return None, [f"{REGISTRY}: items must be a list"]

    issues = date_issues(registry, REGISTRY)
    seen_ids, seen_urls, paper_ids = set(), set(), set()
    for number, item in enumerate(registry["items"]):
        context = f"{REGISTRY}: items[{number}]"
        if not isinstance(item, dict):
            issues.append(f"{context}: item must be an object")
            continue
        for field in REQUIRED:
            if field not in item:
                issues.append(f"{context}: missing required field {field}")
            elif field in ("source_version", "checked_on") and item[field] is None:
                continue
            elif not isinstance(item[field], str) or not item[field].strip():
                issues.append(f"{context}.{field}: expected a nonempty string"
                              + (" or null" if field in ("source_version", "checked_on") else ""))
        aliases = item.get("aliases", [])
        if not isinstance(aliases, list) or any(not isinstance(alias, str) for alias in aliases):
            issues.append(f"{context}.aliases: expected a list of strings")

        identity, canonical = item.get("id"), item.get("canonical_url")
        if isinstance(identity, str):
            if identity in seen_ids:
                issues.append(f"{context}: duplicate id {identity}")
            seen_ids.add(identity)
            if identity in (".", "..") or "/" in identity or "\\" in identity:
                issues.append(f"{context}.id: expected a filename-safe identity")
        if isinstance(canonical, str):
            if canonical in seen_urls:
                issues.append(f"{context}: duplicate canonical_url {canonical}")
            seen_urls.add(canonical)

        if item.get("kind") != "paper" or not isinstance(identity, str):
            continue
        paper_ids.add(identity)
        expected = f"papers/{identity}.md"
        url = parsed_url(canonical) if isinstance(canonical, str) else None
        if (url is None or url.scheme != "https" or url.netloc != "github.com"
                or unquote(url.path) != GITHUB_PATH + expected or url.query or url.fragment):
            issues.append(f"{context}.canonical_url: expected GitHub path {expected}")
        if not (root / expected).is_file():
            issues.append(f"{expected}: missing card for registry paper {identity}")

        source = item.get("source")
        source_url = parsed_url(source) if isinstance(source, str) else None
        if source_url and source_url.hostname in {
                "arxiv.org", "www.arxiv.org", "export.arxiv.org",
                "alphaxiv.org", "www.alphaxiv.org"}:
            match = re.fullmatch(
                r"/(?:abs|pdf|html|overview)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?/?",
                source_url.path,
            )
            if match is None or identity != "arxiv-" + match.group(1):
                issues.append(f"{context}.source: source identity does not agree with {identity}")

    for card in sorted((root / "papers").glob("*.md")):
        if card.name != "README.md" and card.stem not in paper_ids:
            issues.append(f"papers/{card.name}: no registry entry")
    return registry, issues


def cell(value):
    """Escape table syntax while retaining the registry's source wording."""
    if value is None:
        return ""
    return (value.replace("\\", "\\\\").replace("|", "\\|")
            .replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>"))


def render_index(registry):
    papers = sorted((item for item in registry["items"] if item["kind"] == "paper"),
                    key=lambda item: item["id"])
    papers.sort(key=lambda item: item["checked_on"] or "", reverse=True)
    lines = [
        "# 论文速查表", "",
        "<!-- Generated by python scripts/knowledge_base.py index; do not edit by hand. -->", "",
        "数据源：[archive/registry.json](../archive/registry.json)。"
        "仅收录 `kind=paper` 的本仓库论文卡片，产业信号不在此表。", "",
        f"Total papers: **{len(papers)}**。按 `checked_on` 从新到旧排列，同日按 ID 排列，未知日期置后。", "",
        "核验范围直接保留 registry 原文，不升级证据含义；版本或日期空白表示 registry 记录为 null（未知）。"
        "可用标题、别名或主题搜索。", "",
        "| 标题 | 别名 | 主题 | source_version | checked_on | verification_scope |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in papers:
        title = cell(item["title"]).replace("[", "\\[").replace("]", "\\]")
        values = [f"[{title}]({item['id']}.md)",
                  "; ".join(cell(alias) for alias in item.get("aliases", [])),
                  *(cell(item[field]) for field in
                    ("topic", "source_version", "checked_on", "verification_scope"))]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines) + "\n"


def prose_lines(text):
    fence = None
    math_end = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            run, rest = marker.groups()
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not rest.strip():
                fence = None
            continue
        if fence is not None:
            continue
        line = re.sub(r"(`+).*?\1", "", line)
        if math_end:
            end = line.find(math_end)
            if end < 0:
                continue
            line = line[end + len(math_end):]
            math_end = None
        # Keep ordinary prose around $$...$$ and \[...\] blocks visible.
        while match := re.search(r"(?<!\\)(\$\$|\\\[)", line):
            close = "$$" if match.group() == "$$" else "\\]"
            end = line.find(close, match.end())
            if end < 0:
                math_end = close
                line = line[:match.start()]
                break
            line = line[:match.start()] + line[end + len(close):]
        line = re.sub(r"(?<!\\)\$(?!\$).*?(?<!\\)\$|\\\(.*?\\\)", "", line)
        yield number, line


def markdown_issues(root):
    issues, count = [], 0
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if relative.parts[0] == "skills" or ".git" in relative.parts:
            continue
        count += 1
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            issues.append(f"{relative}: cannot read Markdown: {error}")
            continue
        visible = [""] * len(text.splitlines())
        for number, line in prose_lines(text):
            context = f"{relative}:{number}"
            visible[number - 1] = line
            if re.search(r"\\+n", line):
                issues.append(f"{context}: literal backslash-n in prose")
        prose = "\n".join(visible)
        for match in LINK.finditer(prose):
            context = f"{relative}:{prose.count(chr(10), 0, match.start()) + 1}"
            target = match.group("angle") or match.group("plain")
            target = re.sub(r"\\([\\ ()])", r"\1", target)
            url = parsed_url(target)
            if url is None:
                issues.append(f"{context}: invalid link target {target}")
                continue
            if url.scheme or url.netloc or not url.path:
                continue
            local = unquote(url.path)
            destination = root / local.lstrip("/") if local.startswith("/") else path.parent / local
            if not destination.exists():
                issues.append(f"{context}: missing local link target {target}")
    return issues, count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("index", "check"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository root (defaults to this script's repository)")
    args = parser.parse_args()
    root = args.root.resolve()
    registry, issues = load_registry(root)
    expected = render_index(registry) if registry is not None and not issues else None
    markdown_count = 0
    if args.command == "index" and expected is not None:
        try:
            (root / INDEX).parent.mkdir(parents=True, exist_ok=True)
            (root / INDEX).write_text(expected, encoding="utf-8", newline="\n")
        except OSError as error:
            issues.append(f"{INDEX}: cannot write index: {error}")
        else:
            print(f"Wrote {INDEX} ({sum(i['kind'] == 'paper' for i in registry['items'])} papers).")
            return 0
    elif args.command == "check":
        markdown_errors, markdown_count = markdown_issues(root)
        issues.extend(markdown_errors)
        if expected is not None:
            try:
                actual = (root / INDEX).read_bytes().decode("utf-8")
            except (OSError, UnicodeError):
                issues.append(f"{INDEX}: missing or unreadable generated index; run index")
            else:
                if actual != expected:
                    issues.append(f"{INDEX}: stale generated index; run index")
    for issue in issues:
        print(issue)
    if issues:
        print(f"FAILED: {len(issues)} issue(s).")
        return 1
    print(f"OK: {len(registry['items'])} registry entries; {markdown_count} Markdown files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
