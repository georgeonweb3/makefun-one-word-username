"""One Word, One Username, One Reward — make.fun entry.

Writes the entrant's own make.fun username, exactly one word, to
/output/entry.txt. No explanation, no links, no pitch — just the handle.

Entry word: george-codm (11 characters, within the 1-30 gate).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "george-codm"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read-back verification: the file must be byte-for-byte the entry word.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt mismatch: expected {ENTRY.encode('utf-8')!r}, "
        f"got {written!r}"
    )
    # Gate self-check: 1-30 UTF-8 characters, not whitespace-only.
    text = written.decode("utf-8")
    assert 1 <= len(text) <= 30, f"entry length {len(text)} outside 1-30"
    assert text.strip(), "entry must not be whitespace-only"


if __name__ == "__main__":
    main()
