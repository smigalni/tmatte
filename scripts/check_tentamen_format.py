#!/usr/bin/env python3
"""Formatting guardrails for the T-matte tentamen pilot."""
from pathlib import Path
import re
import sys

FILES = [
    Path("docs/t/tentamen-kap1-3-elev.md"),
    Path("docs/t/tentamen-kap1-3-laerer.md"),
]

errors = []
for path in FILES:
    if not path.exists():
        errors.append(f"{path}: file missing")
        continue
    content = path.read_text(encoding="utf-8")

    # Subquestion labels b)-f) may never trail another subquestion on the same line.
    for number, line in enumerate(content.splitlines(), start=1):
        if re.search(r"\\S[ \\t]+[a-f]\\)", line):
            errors.append(
                f"{path}:{number}: possible inline subquestion; put each a), b), c) on its own line"
            )

    # The number line must communicate direction and identify its variable axis.
    if path.name.endswith("-elev.md"):
        if "numberline-arrow" not in content or "marker-start=" not in content or "marker-end=" not in content:
            errors.append(f"{path}: number line is missing arrowheads")
        if not re.search(r'<text[^>]*>x</text>', content):
            errors.append(f"{path}: number line is missing its x-axis label")

        # Any plotted coordinate system must have arrowheads and both axis labels.
        if "graph-axis-arrow" not in content or "marker-end=" not in content:
            errors.append(f"{path}: function graphs are missing axis arrowheads")
        if not re.search(r'<text[^>]*>x</text>', content) or not re.search(r'<text[^>]*>y</text>', content):
            errors.append(f"{path}: function graphs are missing x/y axis labels")

if errors:
    print("\\n".join(errors))
    sys.exit(1)

print("Tentamen formatting checks passed.")
