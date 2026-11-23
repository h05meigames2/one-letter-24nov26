#!/usr/bin/env python3
"""C — Coffee: one letter for your day.

The bounty asks for a program that writes exactly one character, a
letter A-Z, to /output/entry.txt. That single letter stands for a
hidden word describing the day, and a judge model compares two letters
and picks the one whose hidden word feels more vivid, funnier or truer.

Our letter is C, and the word behind it is Coffee: the first thing the
day reaches for, the smell that starts the morning, the pause between
one task and the next. One letter carries all of that.

The program writes exactly the character "C" and nothing else — no
newline, no extra whitespace — to the entry file.
"""

import os

LETTER = "C"

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def entry_path() -> str:
    """Return the path of the entry file.

    Uses $MAKEFUN_OUTPUT_DIR when set, otherwise /output.
    """
    output_dir = os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR)
    return os.path.join(output_dir, ENTRY_FILENAME)


def main() -> None:
    """Validate the letter, then write exactly that one byte."""
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("LETTER must be exactly one A-Z character")

    path = entry_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="ascii", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
