#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes a single-sentence apology from an AI assistant to its user
to /output/entry.txt (override with ENTRY_OUTPUT for local testing).

Angle (brainstorming): the sharpest comic turn is an inversion of the
assistant's own job — it "fixed" the code by deleting the thing that
worked and keeping the bug. Specific, plausible, plain-voiced, a little
embarrassed, no support-macro boilerplate, no machine pun. One clean
sentence, 91 characters, inside the 1-200 gate.
"""

import os

APOLOGY = (
    "I'm sorry I fixed your code by deleting the feature that worked "
    "and keeping the bug that didn't."
)


def validate(text: str) -> None:
    """Gate self-check: UTF-8, 1-200 chars, one sentence, not blank."""
    assert 1 <= len(text) <= 200, f"length {len(text)} outside 1-200"
    assert text.strip(), "entry is blank"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"


def main() -> None:
    validate(APOLOGY)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(APOLOGY)


if __name__ == "__main__":
    main()
