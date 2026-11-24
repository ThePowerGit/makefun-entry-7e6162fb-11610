#!/usr/bin/env python3
"""make.fun entry: "One Sentence for a Traveler from 1800".

The entry is a single sentence imagining how a traveler from 1800 would have
the internet explained to them: a post office the size of the world. The text
lives in entry.txt next to this script; this program copies those exact bytes
to the grading output directory so the judge reads precisely what was written,
with no re-encoding, newline translation, or trimming.

The judge accepts UTF-8 text of 1 to 200 characters that is not only white
space. Before copying, the entry is checked against those rules so a broken
entry fails loudly here instead of quietly at grading time.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt

The output directory defaults to /output and can be overridden with the
MAKEFUN_OUTPUT_DIR environment variable.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

MIN_CHARS = 1
MAX_CHARS = 200


def check_entry(data: bytes) -> str:
    """Return the entry text, raising ValueError if it breaks the gate rules."""
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"entry.txt is not valid UTF-8: {exc}") from exc

    length = len(text)
    if not MIN_CHARS <= length <= MAX_CHARS:
        raise ValueError(
            f"entry.txt is {length} characters; the gate accepts "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry.txt is only white space")

    return text


def main() -> int:
    """Write entry.txt's bytes to <MAKEFUN_OUTPUT_DIR>/entry.txt."""
    source = Path(__file__).resolve().with_name("entry.txt")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")).resolve()

    data = source.read_bytes()
    text = check_entry(data)

    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.txt"
    shutil.copyfile(source, destination)

    print(
        f"wrote {destination} ({len(text)} characters, {len(data)} bytes)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
