#!/usr/bin/env python3
"""Write the one-line entry for make.fun bounty u-pangg7-one-line-of-wonder-ee10fcd8."""

import os
import sys
from pathlib import Path

TEXT = "In the margin of the library book on tides: returned late, still wet."

assert 1 <= len(TEXT) <= 280

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "entry.txt"
output_file.write_bytes(TEXT.encode("utf-8"))

print(len(TEXT), file=sys.stderr)
