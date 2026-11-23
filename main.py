#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Entry: a one-line patch note for a bug in human biology, in the terse
register of a real release note. The joke: the brain's late-night cringe
replay -- a universally recognised bug where an embarrassing memory from
years ago resurfaces at 3am for no reason at all. A specific version, a
specific year, a specific time: it reads like it actually shipped.
"""

import os
import sys

ENTRY = "v2.0.4: fixed a bug where the brain replayed your most embarrassing moment from 2009 at 3:00am for no reason."


def main() -> int:
    """Self-check the gate, then write the line to /output/entry.txt."""
    line = ENTRY.strip()
    if not line:
        print("entry is blank", file=sys.stderr)
        return 1
    if len(line) > 160:
        print(f"entry is {len(line)} chars, over the 160-char cap",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(f"wrote {len(line)} chars to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
