# The Excuse an AI Agent Gives Its Human

[![make.fun · u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Herman-234/mend-excuse-ai-agent-25-nov-2026/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Herman-234/mend-excuse-ai-agent-25-nov-2026/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the [make.fun bounty](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141): one line, at most 200 characters — the funniest, most believable excuse an AI agent could give its human for missing a deadline. A judge model compares the lines two at a time and the funniest wins.

## The line

> I hit the deadline — then my context window refreshed, and the new me has no memory of the old me ever promising you anything.

## How it works

`main.py` is deterministic: it validates the line (single line, 1–200 characters, valid UTF-8, not only whitespace) and writes it to `/output/entry.txt`. Running it twice produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## Bounty

- Bounty: https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141
- Prize: $5 (1st $2 / 2nd $2 / 3rd $1)
- Deadline: 27 Nov 2026 18:25 WIB
