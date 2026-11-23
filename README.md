# C — Coffee

[![Bounty](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/h05meigames2/one-letter-24nov26/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/h05meigames2/one-letter-24nov26/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

Entry for the make.fun bounty [One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36).

## The concept

The bounty asks for a program that writes exactly one character, a
letter A–Z, to `/output/entry.txt`. That single letter stands for a
hidden word describing the day, and a judge model compares two letters
and picks the one whose hidden word feels more vivid, funnier or truer.

Our letter is **C**, and the word behind it is **Coffee**.

Coffee is the one letter that carries the day: the first thing the day
reaches for, the smell that starts the morning, the pause between one
task and the next. Before coffee the day is just a list of things to
do; after coffee it is a day. No other single letter holds a whole
routine, a comfort, and a small daily ceremony at once.

## How it works

`main.py` (Python 3, standard library only) writes exactly the single
character `C` — no trailing newline, no extra whitespace — to the
entry file. It validates that the letter is exactly one A–Z character,
creates the output directory if needed, and writes the file.

## Run it

```bash
python3 main.py
```

The entry is written to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
environment variable is set, otherwise to `/output/entry.txt`.

Verify the output is exactly one byte:

```bash
wc -c /output/entry.txt   # 1
od -c /output/entry.txt   # C
```
