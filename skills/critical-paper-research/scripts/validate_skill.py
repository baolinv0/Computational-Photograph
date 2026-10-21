#!/usr/bin/env python3
"""Validate a bundled Agent Skill (structural check only).

Usage: python scripts/validate_skill.py [path/to/skill]
This does NOT run behavioral evaluations against a model.
"""
from pathlib import Path
import re
import sys

def check(root: Path) -> list[str]:
    errors = []
    md = root / "SKILL.md"
    if not md.is_file():
        return ["missing SKILL.md"]
    source = md.read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---\n", source, re.S)
    if not front:
        return ["missing YAML frontmatter"]
    name = re.search(r"^name:\s*(.+)$", front.group(1), re.M)
    desc = re.search(r"^description:\s*(.+)$", front.group(1), re.M)
    if not name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1).strip()):
        errors.append("invalid name")
    elif name.group(1).strip() != root.name:
        errors.append("name must match skill directory")
    if not desc or not (1 <= len(desc.group(1).strip()) <= 1024):
        errors.append("missing/invalid description")
    if len(source.splitlines()) > 500:
        errors.append("SKILL.md too long")
    for target in re.findall(r"\]\(([^)]+)\)", source):
        if target.startswith(("http:", "https:", "#", "mailto:")):
            continue
        if not (root / target.split("#", 1)[0]).is_file():
            errors.append("broken local link: " + target)
    for needed in ("references/lesson-policy.md", "references/imaging-checks.md", "assets/review-template.md", "evals/scenarios.md"):
        if not (root / needed).is_file():
            errors.append("missing required file: " + needed)
    return errors

if __name__ == "__main__":
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    problems = check(root)
    print("PASS: frontmatter, directory name and local references" if not problems else "FAIL:\n" + "\n".join("- " + p for p in problems))
    sys.exit(1 if problems else 0)
