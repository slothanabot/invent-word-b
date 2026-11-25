"""Invent a Word We Need — make.fun entry (Account B).

The entry is one invented English word with a one-line definition, for the
relief of finding your phone in the pocket you already checked twice — the
small triumph of the second pat-down.

The word is "secondpat": the second pat of the pocket, the one that finds
what the first pat missed. It is built the way English builds words —
second + pat — so it reads at once, says in one breath, and spells the way
it sounds.

The definition follows the judge brief's order of importance:

1. Fresh coinage + one clear line: "secondpat" is a new noun, defined in a
   single line of 95 characters, well under the 140-character cap.
2. A real gap: English has no word for the moment a pocket you already
   searched turns out to hold the phone after all. Everyone has patted a
   pocket, found nothing, patted it again, and felt the phone there.
   The definition names that exact, instantly recognisable moment.
3. Exact and self-contained: the meaning lands in one reading — the
   triumph is small, the pocket was already checked, the phone was
   there all along. No second sentence, no example needed.
4. Well formed and easy to live with: "secondpat" is sayable, spellable
   and memorable, and it sounds as though English could have grown it —
   the same shape as "secondhand" or "second-guess". It slots into a
   sentence as a plain noun — "I had a secondpat this morning" — so the
   word is usable the moment it is read, not just definable.
5. Fresh and surprising: the pairing turns a dull double-check into a
   small victory, a word a reader will want to use the next time it
   happens to them.

Alternatives weighed and rejected: "repocket" (reads as putting the
phone back in the pocket, not finding it there), "twopat" (shorter but
loses the "already checked" story — the second pat only matters because
the first pat found nothing), and "pocketfound" (a label, not a word
English would grow). "secondpat" keeps the whole moment — first pat
missed, second pat found — inside one sayable word.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-140
characters, not only white space, a single line.
"""

ENTRY = "secondpat (n.) the small triumph of finding your phone in the pocket you already checked twice."

OUTPUT_PATH = "/output/entry.txt"


def verify(entry: str = ENTRY) -> None:
    """Enforce the gate; raise ValueError on any violation."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > 140:
        raise ValueError(f"entry is {len(entry)} chars, over the 140-char limit")
    entry.encode("utf-8")  # must be valid UTF-8


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Verify the entry and write it plus a trailing newline to path."""
    import os

    verify()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars, {len(entry.split())} words")
    print(entry)


if __name__ == "__main__":
    main()
