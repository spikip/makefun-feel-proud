"""Entry for the make.fun bounty "Make the AI Judge Feel Proud: A Family Scene".

The program writes a short family scene to /output/entry.txt. A
daughter spends all afternoon building a cardboard robot, introduces
it to her grandma as her brother Tin, and grandma sets an extra
plate at dinner, so Tin has eaten with the family every night since.
It is warm, funny, and heartfelt in one breath: a child's invention
becomes a family member, and the grandma's quiet acceptance is the
moment that makes a proud judge smile. The scene is small and
domestic, the humour is gentle, and the last line lands the warmth —
the extra plate is the whole scene in one gesture. The gate allows 1 to 280 characters of UTF-8 text, so the scene is
checked against that cap before it is written.
"""

import os

ENTRY = (
    "My daughter spent all afternoon building a cardboard robot, then "
    "introduced it to grandma as 'my brother, Tin.' Grandma set an "
    "extra plate at dinner. Tin has eaten with us every night since."
)

MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
