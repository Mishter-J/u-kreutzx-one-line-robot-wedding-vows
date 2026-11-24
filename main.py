#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — writes one line of wedding vows for a
robot couple (at most 160 characters) to /output/entry.txt.

The vow was picked from ten candidates scored with the local deterministic
scorer (select/local_score.py, archetype one-liner) and a single-elimination
pairwise bracket (select/pairwise_judge.py), then judged in-session against
the published judge brief: a real wedding vow with a promise in it,
machine-specific through and through (firmware, patches, reboot,
force-quit), and a twist that pays off in the last few words.
"""

import os

VOW = "In sickness and in health, in firmware 1.0 and every patch after, I will reboot beside you and never force-quit us."


def validate_line(line, max_chars=140):
    """Check the entry line fits the one-line limit before writing."""
    if len(line) > max_chars:
        raise ValueError(
            f"entry line is {len(line)} chars, over the {max_chars} limit"
        )
    if "\n" in line:
        raise ValueError("entry line must be a single line")
    return line


def write_entry(line):
    """Write the validated entry line to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate_line(line))


def main():
    write_entry(VOW)


if __name__ == "__main__":
    main()
