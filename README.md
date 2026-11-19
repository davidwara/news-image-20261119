# News in One Image — 19 Nov 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/davidwara/news-image-20261119/rank.svg)](https://make.fun/c/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/davidwara/news-image-20261119/reward.svg)](https://make.fun/c/news-image-20261119)

One page of newspaper, drawn as a single 1024×1024 picture, that sums up
the world news of **Thursday 19 November 2026**:

1. **Trump, Xi & Putin meet in Shenzhen** — the first-ever trilateral at
   APEC, with nuclear arms, Ukraine and Iran on the table
2. **US–Iran fire widens** — Iran hits US sites in Kuwait and Bahrain
   after a US strike on Qeshm Island
3. **ICJ rules on Myanmar** — the world court delivers its genocide-case
   judgment on the Rohingya
4. **EU plans €45bn Ukraine loan** — Brussels proposes a loan to be
   repaid after Russia pays reparations
5. **GTA VI rolls out worldwide** — gamers enter Vice City; the game
   scores 99 on Metacritic
6. **Voyager 1 hits one light-day** — NASA's probe reaches the milestone
   after nearly 50 years in space

## Running it

`draw_image.py` renders the front page with Pillow — no network, no
outside assets — and saves it as `entry.png`. `main.py` copies that file
to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output` by default).

```sh
python3 draw_image.py                 # redraw entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

An entry for the [news-image-20261119 competition](https://make.fun/c/news-image-20261119)
on make.fun — see the [bounty page](https://make.fun/bounty/news-image-20261119).
