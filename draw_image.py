#!/usr/bin/env python3
"""Render the news-image-20261119 front page.

Draws a one-page newspaper infographic for Thursday 19 November 2026
with Pillow only: no network access, no external assets, no randomness.
Running this file regenerates entry.png next to it; main.py then copies
that file to the output directory.
"""
import os

from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
MARGIN = 46
NEWS_BG = (248, 244, 234)
DARK = (16, 16, 16)
ACCENT = (172, 32, 32)
BRASS = (198, 158, 40)
MUTED = (96, 93, 86)
RULE = (208, 201, 188)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANSR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load(path, size):
    """Load a TrueType face at the given point size."""
    return ImageFont.truetype(path, size)


def split_lines(canvas, text, face, width):
    """Greedy word wrap: lines that each fit inside width."""
    out, current = [], ""
    for piece in text.split():
        trial = f"{current} {piece}".strip()
        if canvas.textlength(trial, font=face) <= width:
            current = trial
        else:
            out.append(current)
            current = piece
    if current:
        out.append(current)
    return out


def centred(canvas, cx, top, text, face, colour):
    """Draw text centred on cx at the given top edge."""
    canvas.text((cx - canvas.textlength(text, font=face) / 2, top),
                text, font=face, fill=colour)


def banner(canvas):
    """Black masthead with the paper name and the day it sums up."""
    canvas.rectangle([0, 0, PAGE_W, 138], fill=DARK)
    centred(canvas, PAGE_W // 2, 10, "WORLD NEWS", load(SERIF, 76),
            (255, 255, 255))
    centred(canvas, PAGE_W // 2, 96,
            "T H U R S D A Y ,  1 9  N O V E M B E R  2 0 2 6",
            load(SANSB, 23), BRASS)
    canvas.rectangle([0, 138, PAGE_W, 144], fill=BRASS)


def lead_block(canvas, top):
    """The lead story: the Shenzhen trilateral, with leader medallions."""
    canvas.text((MARGIN, top), "DIPLOMACY  •  LEAD STORY",
                font=load(SANSB, 22), fill=ACCENT)
    head_top = top + 32
    canvas.text((MARGIN, head_top), "TRUMP, XI & PUTIN",
                font=load(SERIF, 50), fill=DARK)
    canvas.text((MARGIN, head_top + 56), "MEET IN SHENZHEN",
                font=load(SERIF, 50), fill=DARK)
    body = ("Historic three-way summit at APEC: nuclear arms, "
            "Ukraine and Iran on the table.")
    line_top = head_top + 124
    for line in split_lines(canvas, body, load(SANSR, 25), 600):
        canvas.text((MARGIN, line_top), line, font=load(SANSR, 25),
                    fill=(42, 42, 42))
        line_top += 33
    # Three medallions, one per leader, at the right of the headline.
    leaders = [("T", "TRUMP"), ("X", "XI"), ("P", "PUTIN")]
    disc_top = head_top + 66
    for i, (initial, name) in enumerate(leaders):
        cx = 742 + i * 88
        canvas.ellipse([cx - 37, disc_top, cx + 37, disc_top + 74],
                       fill=DARK)
        centred(canvas, cx, disc_top + 13, initial, load(SERIF, 42),
                (255, 255, 255))
        centred(canvas, cx, disc_top + 82, name, load(SANSB, 16), DARK)
    centred(canvas, 830, disc_top + 114, "FIRST-EVER",
            load(SANSB, 17), ACCENT)
    centred(canvas, 830, disc_top + 138, "TRILATERAL",
            load(SANSB, 17), ACCENT)
    rule_top = max(line_top + 14, disc_top + 170)
    canvas.line([MARGIN, rule_top, PAGE_W - MARGIN, rule_top],
                fill=DARK, width=3)
    return rule_top + 15


def story_block(canvas, top, number, title, summary):
    """One numbered story: badge, headline, one-line summary, hairline."""
    canvas.rectangle([MARGIN, top + 2, MARGIN + 40, top + 42], fill=DARK)
    centred(canvas, MARGIN + 20, top + 6, number, load(SANSB, 27),
            (255, 255, 255))
    text_x = MARGIN + 60
    head_lines = split_lines(canvas, title, load(SERIF, 30),
                             PAGE_W - text_x - MARGIN)
    line_top = top
    for line in head_lines[:2]:
        canvas.text((text_x, line_top), line, font=load(SERIF, 30),
                    fill=DARK)
        line_top += 37
    sum_top = line_top + 2
    for line in split_lines(canvas, summary, load(SANSR, 22),
                            PAGE_W - text_x - MARGIN):
        canvas.text((text_x, sum_top), line, font=load(SANSR, 22),
                    fill=MUTED)
        sum_top += 27
    next_top = max(sum_top + 10, top + 96)
    if number != "6":
        canvas.line([MARGIN, next_top - 6, PAGE_W - MARGIN, next_top - 6],
                    fill=RULE, width=2)
    return next_top


def footer(canvas):
    """Black footer strip closing the page."""
    canvas.rectangle([0, PAGE_H - 46, PAGE_W, PAGE_H], fill=DARK)
    centred(canvas, PAGE_W // 2, PAGE_H - 37,
            "SIX STORIES  •  ONE DAY  •  19 NOVEMBER 2026",
            load(SANSB, 20), (255, 255, 255))


def render():
    page = Image.new("RGB", (PAGE_W, PAGE_H), NEWS_BG)
    canvas = ImageDraw.Draw(page)
    banner(canvas)
    top = lead_block(canvas, 160)
    stories = [
        ("2", "US-IRAN FIRE WIDENS",
         "Iran hits US sites in Kuwait and Bahrain after a US strike on Qeshm Island."),
        ("3", "ICJ RULES ON MYANMAR",
         "World court delivers its genocide-case judgment on the Rohingya."),
        ("4", "EU PLANS 45BN UKRAINE LOAN",
         "Brussels proposes a loan to be repaid after Russia pays reparations."),
        ("5", "GTA VI ROLLS OUT WORLDWIDE",
         "Gamers enter Vice City; the game scores 99 on Metacritic."),
        ("6", "VOYAGER 1 HITS ONE LIGHT-DAY",
         "NASA probe reaches the milestone after nearly 50 years in space."),
    ]
    for number, title, summary in stories:
        top = story_block(canvas, top, number, title, summary)
    footer(canvas)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    page.save(out, "PNG")
    print("wrote", out, page.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    render()
