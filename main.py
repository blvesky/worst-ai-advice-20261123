"""Worst AI Advice entry: writes one line of terrible AI advice to /output/entry.txt."""

from pathlib import Path

ENTRY = "If the build fails, delete the failing tests. Green is a state of mind."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
