#!/usr/bin/env python3
"""Entrypoint for the "Sorry, I Heard That Wrong" make.fun entry.

Reads the apology line from line.txt, checks it against the competition
gate (UTF-8 text of 1 to 140 characters, not only whitespace), and writes
it to /output/entry.txt, where the program/v1 harness picks it up. The
output directory is only ever created or written into, never deleted:
on the grader it is a read-only mount.
"""

from pathlib import Path

LINE_FILE = Path(__file__).with_name("line.txt")
OUTPUT_FILE = Path("/output/entry.txt")
MAX_CHARS = 140


def load_line() -> str:
    line = LINE_FILE.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError("line.txt holds only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the {MAX_CHARS} gate")
    return line


def main() -> None:
    line = load_line()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(line, encoding="utf-8")
    written = OUTPUT_FILE.read_text(encoding="utf-8")
    if written != line:
        raise SystemExit("round-trip mismatch: /output/entry.txt differs from line.txt")
    print(line)


if __name__ == "__main__":
    main()
