#!/usr/bin/env python3
"""Send one job title, 60 characters at most, the weirdest you can think of, to /output/entry.txt.

The title is written exactly as given: 48 Unicode code points,
inside the competition gate of 1-60. Python 3, standard library
only, no network.
"""

import os

TEXT = "Senior Vice President of Apologising to Printers"

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
