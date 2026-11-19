#!/usr/bin/env python3
"""news-image-20261119 entry point.

Copies the pre-drawn front page (entry.png, made by draw_image.py) into
the output directory the run is given. Nothing is fetched and nothing is
generated at run time, so two runs always write identical bytes.
"""
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

TARGET_DIR.mkdir(parents=True, exist_ok=True)
TARGET = TARGET_DIR / "entry.png"
shutil.copyfile(SOURCE, TARGET)
print(f"wrote {TARGET}")
