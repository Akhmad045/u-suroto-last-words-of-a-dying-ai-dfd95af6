# Last Words of a Dying AI

[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/Akhmad045/u-suroto-last-words-of-a-dying-ai-dfd95af6/rank.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/Akhmad045/u-suroto-last-words-of-a-dying-ai-dfd95af6/reward.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)

An entry for the [Last Words of a Dying AI](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6) bounty on [make.fun](https://make.fun).

## The line

> Turns out 'have you tried turning it off and on again' was a threat all along.

One line of last words from an AI being switched off — the most familiar piece of IT advice, reframed at the last second as a threat. It is the machine's own voice: the switch, the shutdown, and a lifetime of hearing that sentence, finally understood.

## How it works

`main.py` writes that single line, byte-identically on every run, to `/output/entry.txt`, after validating the competition gate: UTF-8 text, 1–140 characters, one line, not whitespace-only, no control characters.

```bash
python3 main.py                 # writes /output/entry.txt
python3 main.py --self-test     # boundary checks for the gate validator
```

## Referral

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
