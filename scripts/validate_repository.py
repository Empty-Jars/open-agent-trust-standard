#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "CHARTER.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "SECURITY.md", "GOVERNANCE.md", "MAINTAINERS.md", "AGENTS.md",
    "LICENSE.md", "LICENSES/Apache-2.0.txt", "LICENSES/Community-Spec-1.0.md",
    "NOTICE", "DCO",
    ".github/PULL_REQUEST_TEMPLATE.md", ".github/ISSUE_TEMPLATE/proposal.yml",
]
errors = []
for relative in REQUIRED:
    path = ROOT / relative
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        errors.append(f"missing or empty: {relative}")
for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    if chr(0) in text:
        errors.append(f"NUL byte in {path.relative_to(ROOT)}")
    if not text.endswith("\n"):
        errors.append(f"missing final newline: {path.relative_to(ROOT)}")
if errors:
    print("Foundation validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"Foundation validation passed ({len(list(ROOT.rglob('*.md')))} Markdown files).")
