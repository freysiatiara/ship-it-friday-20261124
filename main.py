#!/usr/bin/env python3
"""Ship It Friday — make.fun bounty entry.

Writes the funniest one-line git commit message an AI coding agent
writes right before breaking production on a Friday, to the output
file the grader expects.
"""

import os
import sys

LINE = (
    "feat: ship to prod Friday \u2014 tests pass in my sandbox, "
    "prod is basically the same thing"
)


def main() -> int:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

    if not (1 <= len(LINE) <= 159):
        print(
            f"error: entry line is {len(LINE)} characters, "
            "must be 1..159",
            file=sys.stderr,
        )
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: entry line must not be only whitespace", file=sys.stderr)
        return 1

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
