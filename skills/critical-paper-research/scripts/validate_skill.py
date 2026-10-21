#!/usr/bin/env python3
"""Structural checks only; not a substitute for agent-behavior evaluation."""
from pathlib import Path
import re
import sys

def check(root):
    errors=[]
    p=root/"SKILL.md"
    if not p.is_file(): return ["missing SKILL.md"]
    s=p.read_text(encoding="utf-8")
    f=re.match(r"\\A---\\n(.*?)\\n---\\n",s,re.S)
    if not f: return ["missing YAML frontmatter"]
    n=re.search(r"^name:\\s*(.+)$",f.group(1),re.M)
    d=re.search(r"^description:\\s*(.+)$",f.group(1),re.M)
    if not n or n.group(1).strip()!=root.name: errors.append("name/path mismatch")
    if not d: errors.append("missing description")
    for link in re.findall(r"\\]\\(([^)]+)\\)",s):
        if link.startswith(("http:","https:","#","mailto:")):continue
        if not (root/link.split("#",1)[0]).is_file(): errors.append("missing reference "+link)
    return errors

if __name__=="__main__":
    root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
    errs=check(root)
    print("PASS: structural links and metadata" if not errs else "FAIL: "+"; ".join(errs))
    sys.exit(1 if errs else 0)
