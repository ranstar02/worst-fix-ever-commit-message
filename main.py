#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit-message line to /output/entry.txt.
"""

from pathlib import Path

def get_entry() -> str:
    # One line, no trailing newline: the fix trades a timeout for no
    # password check at all, so everyone gets in instantly.
    return "fix: login timeout by skipping the password check, logins are instant now for everyone"


def main() -> None:
    entry = get_entry()
    assert "\n" not in entry and 1 <= len(entry) <= 100
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
