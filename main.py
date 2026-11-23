"""Dad Joke Showdown entry: write one dad joke to /output/entry.txt.

Stdlib only, no network, deterministic: the same bytes on every run.
The joke is a single Q&A dad joke, 57 characters, punchline at the end.
"""

import os

JOKE = "Why did Dad put his car in the oven? He wanted a hot rod."


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print("wrote %s (%d characters)" % (out, len(JOKE)))


if __name__ == "__main__":
    main()
