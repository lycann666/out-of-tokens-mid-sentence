#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun program/v1 entry.

Writes the entry line verbatim to entry.txt with no trailing newline.
"""

import os

ENTRY = "Error 402: token budget exhausted. The rest of this answer has been outsourced to your imagination."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
