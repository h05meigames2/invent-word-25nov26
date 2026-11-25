#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented English word plus a one-line definition to
/output/entry.txt. The entry must be 1-140 characters, a single line
of UTF-8 text, with no trailing newline.
"""

import os

ENTRY = (
    # "dotdread": the dread of watching someone's typing dots while
    # waiting for a reply that keeps not coming.
    "dotdread — the tense wait for a reply while someone's typing "
    "dots appear, vanish, then appear again."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(text: str) -> None:
    """Check the entry against the bounty gate rules."""
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
