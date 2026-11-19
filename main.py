#!/usr/bin/env python3
"""news-image-20261119 entrypoint: copy the entry image to the output dir.

The image is drawn by draw_image.py and stored in this repository as
entry.png; this program just copies it to /output/entry.png (or
$MAKEFUN_OUTPUT_DIR/entry.png). Deterministic, no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(
    os.path.join(HERE, "entry.png"),
    os.path.join(OUT_DIR, "entry.png"),
)
print("wrote", os.path.join(OUT_DIR, "entry.png"))
