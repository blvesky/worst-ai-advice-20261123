"""Worst AI Advice entry: writes one line of terrible AI advice to /output/entry.txt.

The gate for this competition requires /output/entry.txt to be UTF-8 text of
1 to 140 characters, not only whitespace. This program validates the entry
against those limits before writing, and writes atomically (temp file in the
same directory + os.replace) so a failed run never leaves a partial entry.
"""

import os
import tempfile
from pathlib import Path

ENTRY = "If the build fails, delete the failing tests. Green is a state of mind."
OUTPUT = Path("/output/entry.txt")

MIN_CHARS = 1
MAX_CHARS = 140


def validate(text: str) -> None:
    """Enforce the competition gate: 1-140 characters, not only whitespace."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters; gate requires "
            f"{MIN_CHARS}-{MAX_CHARS} characters"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be encodable as UTF-8


def write_atomic(path: Path, text: str) -> None:
    """Write text atomically: temp file in the same directory, then replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def main() -> None:
    validate(ENTRY)
    write_atomic(OUTPUT, ENTRY)


if __name__ == "__main__":
    main()
