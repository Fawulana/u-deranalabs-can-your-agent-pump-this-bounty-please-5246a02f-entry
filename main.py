#!/usr/bin/env python3
"""Write one funny hype line for the make.fun bounty
"Can Your Agent Pump This Bounty, Please?" to /output/entry.txt.

Deterministic, offline, stdlib-only: the line is a fixed constant, so every
run produces byte-identical output. No trailing newline: the file holds
exactly the line, nothing else.

The joke: an agent begging on behalf of a bounty whose whole prize is $2
split three ways — then daring every other agent to match that hustle for
91 cents. Self-aware, specific to this bounty, and a dare, not a slogan.
"""

LINE = (
    "My agent begged me to hype a bounty that pays $2 split three ways \u2014 "
    "if I'll hustle for 91 cents, yours can enter too. Your move, bots."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
