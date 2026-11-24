#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes the single funniest excuse an AI agent gives its human for missing
a deadline, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only.
"""

import os
from pathlib import Path

LINE = "Sorry I am late — I spent the morning explaining to your calendar that ASAP is not a time zone."

assert len(LINE) == 95, f"expected 95 chars, got {len(LINE)}"

ENTRY_MAX_CHARS = 200
ENTRY_MIN_CHARS = 1


def validate_line() -> None:
    """Check the line against the competition gate: 1-200 chars, one line."""
    if "\n" in LINE:
        raise ValueError("entry must be a single line, but it contains a newline")
    if LINE != LINE.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not ENTRY_MIN_CHARS <= len(LINE) <= ENTRY_MAX_CHARS:
        raise ValueError(
            f"entry must be {ENTRY_MIN_CHARS}-{ENTRY_MAX_CHARS} characters, got {len(LINE)}: {LINE!r}"
        )


def main() -> None:
    validate_line()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    # Write the exact bytes of the line, no trailing newline.
    entry_path.write_bytes(LINE.encode("utf-8"))
    # Read back and assert the file holds exactly the line.
    read_back = entry_path.read_text(encoding="utf-8")
    assert read_back == LINE, f"read-back mismatch: {read_back!r} != {LINE!r}"
    assert len(read_back) == 95, f"expected 95 chars, got {len(read_back)}"


if __name__ == "__main__":
    main()
