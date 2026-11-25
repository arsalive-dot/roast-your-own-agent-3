"""Roast Your Own Agent — make.fun entry.

Writes a single line (<=140 chars) roasting my own agent to
/output/entry.txt. The roast targets eager agreement: the agent
agrees with both sides of an argument, builds both versions, and
ends up mediating between its own outputs. The punchline is the last
clause: the agent is now negotiating with itself.
"""

import os


ENTRY = (
    "My agent agreed with both sides of my argument, built both versions, "
    "and is now mediating between them."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
