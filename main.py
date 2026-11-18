#!/usr/bin/env python3
"""Tuesday 17 November 2026 world news in one image.

Writes the front-page image to the output directory. The image is a
static asset committed in this repository (entry.png); this program only
copies its bytes, so every run produces identical output. No network
access, no randomness, no clock reads: the output is fully deterministic.
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"Wrote {dst} ({size} bytes)")


if __name__ == "__main__":
    sys.exit(main())
