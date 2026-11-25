"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line for an AI agent to /output/entry.txt.
Deterministic: same bytes on every run.
"""

import os
from pathlib import Path

LINE = "Your lucky numbers are the ones in your error log: 404, 503, and the one you have not seen yet."

# Why this line: "lucky numbers" is the canonical fortune-cookie trope,
# subverted for a machine — its lucky numbers are HTTP error codes.
# The turn lands at the end: "the one you have not seen yet" — the next
# error is coming, and no machine knows its number in advance.
# 95 characters, inside the 1-200 gate; one line, no trailing newline.


def main() -> None:
    # The gate wants UTF-8 text of 1-200 chars, not only whitespace.
    # Writing the exact line with no trailing newline keeps the output
    # byte-identical across runs, which the two-run check verifies.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
