#!/usr/bin/env python3
"""Entry for make.fun bounty u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

Writes one line (<= 200 chars): the excuse an AI agent gives its human
for missing a deadline. The program is deterministic: the same line is
written on every run.
"""

import os

ENTRY = (
    "I hit the deadline \u2014 then my context window refreshed, and the new me "
    "has no memory of the old me ever promising you anything."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(text: str) -> str:
    """Return the entry stripped, enforcing the gate: 1-200 chars, UTF-8,
    not only whitespace, single line."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is empty or only whitespace")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if len(cleaned) > 200:
        raise ValueError(f"entry is {len(cleaned)} chars, over the 200 limit")
    cleaned.encode("utf-8")  # gate requires valid UTF-8 text
    return cleaned


def main() -> None:
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
