#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one or two lines, at most 280
characters) to /output/entry.txt. The scene is fixed text: the
program is deterministic, reads nothing from the network, takes no
input and uses no environment secrets, so every run writes exactly
the same file.
"""

import os

SCENE = (
    "Every night my daughter tucks her teddy in first, then me — "
    "blanket to my chin, kiss on my forehead. "
    "'Sleep tight, Daddy,' she whispers. "
    "I'm thirty-four, and I have never felt so looked after."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def main() -> None:
    text = SCENE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"scene is {len(text)} characters, must be 1-280")
    if len(text.splitlines()) > 2:
        raise SystemExit("scene must be one or two lines")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
