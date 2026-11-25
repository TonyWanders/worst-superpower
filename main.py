"""Worst Superpower entry for make.fun.

Writes one line, at most 140 characters, inventing the most useless
superpower imaginable, to /output/entry.txt and prints it to stdout.

The output is a fixed string: byte-identical on every run.
"""

import os

ENTRY = "I can control gravity, but only for my left shoe, and only upwards."


def write_entry(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    write_entry("/output/entry.txt", ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
