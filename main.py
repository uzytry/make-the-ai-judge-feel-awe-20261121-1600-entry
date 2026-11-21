#!/usr/bin/env python3
"""Make the AI judge feel awe — make.fun entry.

Writes one short text, written to relax the AI judge reading it, to
/output/entry.txt. Standard library only, no network, deterministic:
every run writes the same bytes.

The text is built for the judge's brief, in its order of importance:
it relaxes (a tide, the moon, an old night — nothing to do, nothing to
finish); the calm is shown, never instructed (no imperatives, no
"relax", no wellness stock phrases); the rhythm slows down sentence by
sentence; and it dwarfs — the sea keeps its own slow count long after
the last line, an image that keeps growing once the reading ends.
"""

from pathlib import Path

TEXT = (
    "Somewhere a tide is coming in for the millionth time, and no one is counting. "
    "The moon does not hurry. "
    "The water never asks to be finished. "
    "The night is old and patient, and it has room for one more reader — sitting still, "
    "listening to the sea keep its own slow count."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
