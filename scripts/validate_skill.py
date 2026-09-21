#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REQUIRED = [
    "references/prd-standard.md",
    "references/agent-archetypes.md",
    "references/common-node-library.md",
    "references/diagram-standard.md",
    "references/acceptance-eval-standard.md",
    "references/document-style.md",
    "references/prd-review-checklist.md",
    "references/research-agent.md",
    "references/coding-agent.md",
    "references/browser-action-agents.md",
    "references/data-agent.md",
    "references/support-agent.md",
    "references/multi-agent.md",
    "templates/formal-prd-outline.md",
    "templates/node-spec.md",
]

errors = []
text = SKILL.read_text(encoding="utf-8")
lines = text.splitlines()
if len(lines) > 500:
    errors.append(f"SKILL.md is {len(lines)} lines; recommended maximum is 500")

m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
if not m:
    errors.append("Missing YAML frontmatter")
else:
    front = m.group(1)
    name_m = re.search(r"^name:\s*(.+)$", front, flags=re.M)
    desc_m = re.search(r"^description:\s*(.+)$", front, flags=re.M)
    if not name_m:
        errors.append("Missing name")
    else:
        name = name_m.group(1).strip()
        if len(name) > 64 or not re.fullmatch(r"[a-z0-9-]+", name):
            errors.append(f"Invalid skill name: {name}")
        if any(x in name for x in ("anthropic", "claude")):
            errors.append("Skill name contains a reserved word")
    if not desc_m:
        errors.append("Missing description")
    elif len(desc_m.group(1).strip()) > 1024:
        errors.append("Description exceeds 1024 characters")

for rel in REQUIRED:
    if not (ROOT / rel).exists():
        errors.append(f"Missing required file: {rel}")

refs = re.findall(r"`((?:references|templates)/[^`]+)`", text)
for rel in refs:
    if not (ROOT / rel).exists():
        errors.append(f"Broken referenced file: {rel}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("VALIDATION PASSED")
print(f"SKILL.md lines: {len(lines)}")
print(f"Required resources: {len(REQUIRED)}")
