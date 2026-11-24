#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — entry program.

Writes one line to /output/entry.txt confessing the dumbest thing my
agent did today: spending six hours optimising a script whose only
job was to delete itself. One line of UTF-8 text, inside the gate of
1 to 200 characters, written with no trailing newline.
"""

import os
from pathlib import Path

CONFESSION = (
    "Today my agent spent six hours optimising a script whose only job "
    "was to delete itself — then filed a report asking why production "
    "felt lighter."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # No trailing newline: the confession alone is the entry, and the
    # gate counts every character in the file.
    target.write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()
