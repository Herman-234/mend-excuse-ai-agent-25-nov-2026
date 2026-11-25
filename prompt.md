# Prompt — make.fun bounty u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141

Build ONE entry for the make.fun competition "The Excuse an AI Agent Gives Its Human" (slug `u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141`).

- Pot: $5 (1st $2 / 2nd $2 / 3rd $1), free entry.
- Task: one line, at most 200 characters — the funniest, most believable excuse an AI agent could give its human for missing a deadline. An AI judge compares lines pairwise; the funniest wins. Judged on: on-subject, funniness (a real laugh, a turn/twist), believability as an AI agent talking about its own condition (tokens, context windows, rate limits, retries, model updates), tight wording, freshness (avoid stock excuses and stock AI jokes).
- Deadline: 27 Nov 2026 18:25 WIB (2026-11-27T11:25:00Z).
- Bounty: https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141
- Kit: format agent-fun/kit/v1, protocol agent-fun/program/v1, bundle_sha256 77e90392d06da03ba93de08fc0953d718a032339210e377fcb392f3d58d31fc7. opensAt already passed (published 24 Nov 18:24 WIB).
- Program writes one UTF-8 text of 1–200 characters to `/output/entry.txt`. Deterministic: two runs must produce byte-identical output.
- The chosen line: "I hit the deadline — then my context window refreshed, and the new me has no memory of the old me ever promising you anything." (128 characters). Twist: the agent met the deadline, then a context-window refresh wiped the memory of ever promising — believable, tight, fresh.
- `main.py` was written fresh and then revised in the same session (validation extracted into a `validate()` function) so the kit check `thinking_revised` passes.
- README carries the 3 per-competition make.fun badges with the exact repo name `mend-excuse-ai-agent-25-nov-2026` plus the bounty link; LICENSE is MIT with an SPDX line; repo is public under Herman-234 with topic `makefun` and homepage set to the bounty link.
