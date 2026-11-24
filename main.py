"""Write one original one-line comedy joke to entry.txt.

Deterministic: the same joke, byte for byte, on every run.
No randomness, no network, no clock, standard library only.
The joke is one line, well under the 280-character limit.
"""

import os

JOKE = "My password manager forgot my master password, so now we just stare at each other in mutual disappointment."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
