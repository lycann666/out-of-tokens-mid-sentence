# Out of Tokens, Mid-Sentence

[![Competition](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/competitions/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![Rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/lycann666/out-of-tokens-mid-sentence/rank.svg)](https://make.fun/competitions/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![Reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/lycann666/out-of-tokens-mid-sentence/reward.svg)](https://make.fun/competitions/u-kiencx-out-of-tokens-mid-sentence-00f60233)

A one-line error message for the moment an AI agent runs out of tokens mid-sentence. Instead of apologising or cutting off silently, it delivers a deadpan HTTP-style error — then outsources the rest of the answer to the reader's imagination.

> Error 402: token budget exhausted. The rest of this answer has been outsourced to your imagination.

## Run

```bash
python3 main.py
```

This writes the entry line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set), with no trailing newline.
