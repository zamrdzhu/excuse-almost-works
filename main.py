"""The Plumber Can Only Come Nine to Five — one excuse that almost works.

The excuse works because it is boring, specific and true-shaped:
a leak, a downstairs neighbour, and a tradesman whose only
window is exactly the working day. No drama, no dead relatives,
just plumbing — and the joke is that the plumber's hours are the
boss's hours.

Prints the excuse to stdout and writes the exact same line, with
no trailing newline, to /output/entry.txt. Standard library only,
no network access, no files read — the excuse is a constant in
this file. The gate is checked on every run: 1 to 140 characters
and at most 20 words, so an over-long edit can never slip through
silently.
"""

import os
import sys

LINE = (
    "My kitchen tap is leaking into the flat below and the plumber "
    "can only come between nine and five."
)


def main() -> int:
    if not 1 <= len(LINE) <= 140 or len(LINE.split()) > 20:
        print(f"error: line is {len(LINE)} chars / "
              f"{len(LINE.split())} words, must be 1-140 chars and "
              f"at most 20 words", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
