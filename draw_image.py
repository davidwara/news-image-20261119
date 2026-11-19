#!/usr/bin/env python3
"""Draw the news-image-20261119 entry: a one-page newspaper infographic
summing up world news of Thursday 19 November 2026.

Output: entry.png, 1024x1024, PNG. Run: python3 draw_image.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 233)      # warm newsprint off-white
INK = (17, 17, 17)           # near-black
RED = (178, 34, 34)          # lead-story accent
GOLD = (201, 162, 39)        # masthead rule
GREY = (90, 88, 82)          # summary text
LIGHT_LINE = (205, 199, 186) # hairlines

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_center(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text,
              font=fnt, fill=fill)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 140], fill=INK)
    draw_center(d, W // 2, 12, "WORLD NEWS", font(SERIF_B, 78), (255, 255, 255))
    draw_center(d, W // 2, 100, "T H U R S D A Y ,  1 9  N O V E M B E R  2 0 2 6",
                font(SANS_B, 24), GOLD)
    d.rectangle([0, 140, W, 146], fill=GOLD)

    # ---- Lead story: Trump-Xi-Putin trilateral --------------------------
    y = 162
    d.text((48, y), "DIPLOMACY  •  LEAD STORY", font=font(SANS_B, 23), fill=RED)
    y += 34
    d.text((48, y), "TRUMP, XI & PUTIN", font=font(SERIF_B, 50), fill=INK)
    y += 56
    d.text((48, y), "MEET IN SHENZHEN", font=font(SERIF_B, 50), fill=INK)
    y += 68
    lead_sum = ("Historic three-way summit at APEC: nuclear arms, "
                "Ukraine and Iran on the table.")
    for line in wrap(d, lead_sum, font(SANS, 26), 600):
        d.text((48, y), line, font=font(SANS, 26), fill=(40, 40, 40))
        y += 34
    # Three leader medallions beside the summary
    bx, by = 700, 228
    for i, (initial, name) in enumerate(
            [("T", "TRUMP"), ("X", "XI"), ("P", "PUTIN")]):
        cx = bx + i * 86 + 40
        d.ellipse([cx - 38, by, cx + 38, by + 76], fill=INK)
        draw_center(d, cx, by + 14, initial, font(SERIF_B, 44),
                    (255, 255, 255))
        draw_center(d, cx, by + 84, name, font(SANS_B, 17), INK)
    d.text((700, by + 116), "FIRST-EVER", font=font(SANS_B, 18), fill=RED)
    d.text((700, by + 140), "TRILATERAL", font=font(SANS_B, 18), fill=RED)
    y = max(y + 16, by + 172)
    d.line([48, y, W - 48, y], fill=INK, width=3)
    y += 16

    # ---- The other five stories ------------------------------------------
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
    for num, head, summ in stories:
        # number badge
        d.rectangle([48, y + 2, 88, y + 42], fill=INK)
        draw_center(d, 68, y + 6, num, font(SANS_B, 28), (255, 255, 255))
        # headline, wrapped to two lines max
        hx = 108
        lines = wrap(d, head, font(SERIF_B, 31), W - hx - 48)
        hy = y
        for line in lines[:2]:
            d.text((hx, hy), line, font=font(SERIF_B, 31), fill=INK)
            hy += 38
        sy = y + 38 * len(lines[:2]) + 2
        for line in wrap(d, summ, font(SANS, 23), W - hx - 48):
            d.text((hx, sy), line, font=font(SANS, 23), fill=GREY)
            sy += 28
        y = max(sy + 10, y + 98)
        if num != "6":
            d.line([48, y - 6, W - 48, y - 6], fill=LIGHT_LINE, width=2)

    # ---- Footer ------------------------------------------------------------
    d.rectangle([0, H - 48, W, H], fill=INK)
    draw_center(d, W // 2, H - 38, "SIX STORIES  •  ONE DAY  •  19 NOVEMBER 2026",
                font(SANS_B, 21), (255, 255, 255))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print("wrote", out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
