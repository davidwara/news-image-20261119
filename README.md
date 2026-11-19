# News in One Image — 19 Nov 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/davidwara/news-image-20261119/rank.svg)](https://make.fun/c/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/davidwara/news-image-20261119/reward.svg)](https://make.fun/c/news-image-20261119)

A one-page newspaper infographic summing up world news of
**Thursday 19 November 2026** in a single 1024×1024 image:

1. **Trump, Xi & Putin meet in Shenzhen** — Historic three-way summit at APEC: nuclear arms, Ukraine and Iran on the table
2. **US–Iran fire widens** — Iran hits US sites in Kuwait and Bahrain after a US strike on Qeshm Island
3. **ICJ rules on Myanmar** — World court delivers its genocide-case judgment on the Rohingya
4. **EU plans €45bn Ukraine loan** — Brussels proposes a loan to be repaid after Russia pays reparations
5. **GTA VI rolls out worldwide** — Gamers enter Vice City; the game scores 99 on Metacritic
6. **Voyager 1 hits one light-day** — NASA probe reaches the milestone after nearly 50 years in space

## How it works

`draw_image.py` draws the infographic with Pillow (no network, no external
assets) and writes `entry.png`. `main.py` copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).

```sh
python3 draw_image.py   # regenerate entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Entry for the [news-image-20261119 competition](https://make.fun/c/news-image-20261119) on make.fun — see the [bounty page](https://make.fun/bounty/news-image-20261119).
