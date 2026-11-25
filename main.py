"""Write the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only, no network, fully deterministic.
"""

import os

ENTRY = (
    "The map swore this cul-de-sac was a shortcut, so I believed it, "
    "and frankly the bride looked thrilled to have a getaway car in her vows."
)

assert 1 <= len(ENTRY) <= 200, len(ENTRY)
assert "\n" not in ENTRY


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
