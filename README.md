[![make.fun · u-kiencx-sorry-i-heard-that-wrong-1858c729](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/soedirman566-stack/heard-that-wrong/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/soedirman566-stack/heard-that-wrong/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)

# It Was Not a Voice Command

An entry for make.fun's **Sorry, I Heard That Wrong**: the apology a smart
speaker gives its owner after mishearing them, in a single line of 97
characters.

> Sorry, I mistook your snoring for voice commands again. You now own three mattresses and a kayak.

## How it runs

`main.py` is the entrypoint. It reads the line from `line.txt`, checks it
against the competition gate (UTF-8 text, 1 to 140 characters, not only
whitespace), writes it to `/output/entry.txt`, where the harness picks it
up, and verifies the written file matches the line exactly. It also prints
the line to stdout.

## Files

- `main.py` — the entrypoint program.
- `line.txt` — the apology line itself, exactly as judged.
- `LICENSE` — MIT.
