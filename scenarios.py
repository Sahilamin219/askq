# /// script
# requires-python = ">=3.11"
# dependencies = ["openai>=1.60", "pydantic>=2"]
# ///
"""Runs the scenarios against one household memory (in order, on simulated days) and writes transcripts/.

    OPENAI_API_KEY=... uv run scenarios.py
"""
import json
from datetime import datetime, timedelta
from pathlib import Path

from agent import step

START = datetime(2026, 10, 26, 9, 0)
SCENARIOS = [  # (file, title, day offset, user messages)
    ("1-child-fever-home-care", "New member + new episode, follow-up questions, home care", 0, [
        "My son Aarav has had a fever since last night",
        "He's 6. It was 100.4F this morning, he's still playing and eating, just a bit tired. None of those.",
    ]),
    ("2-parent-chronic-doctor", "Switching member, long-term memory, deterministic doctor handoff, general query", 0, [
        "Papa is 68 and has type 2 diabetes. Since yesterday he's had burning when he urinates.",
        "It's moderate, no fever or back pain. No to all of those, he's alert.",
        "What should he be eating to keep his sugar in check?",
    ]),
    ("3-followup-worsening", "Implicit member via open episode, update attaches to it, worsening -> doctor", 3, [
        "His fever is still there, it touched 102.5 last night and he's eating less",
    ]),
    ("4-emergency", "Red flags short-circuit everything: no questions, fixed emergency message", 4, [
        "My mother suddenly has a crooked face and can't lift her right arm",
    ]),
]

if __name__ == "__main__":
    out = Path("transcripts")
    out.mkdir(exist_ok=True)
    state = {"members": {}, "episodes": [], "turns": []}
    for file, title, day, messages in SCENARIOS:
        lines = [f"# {title}\n"]
        for i, text in enumerate(messages):
            now = START + timedelta(days=day, minutes=5 * i)
            r = step(state, text, now)
            lines += [f"**User** ({now:%a %d %b, %H:%M}): {text}\n",
                      f"> `{r['decision']}` · member=`{r['member']}` · episode=`{r['episode']}`"
                      + (f" · reasons: {'; '.join(r['reasons'])}" if r["reasons"] else "") + "\n",
                      f"**Assistant:** {r['reply']}\n"]
        lines += ["<details><summary>Memory after this scenario</summary>\n",
                  f"```json\n{json.dumps({k: state[k] for k in ('members', 'episodes')}, indent=1)}\n```\n</details>\n"]
        (out / f"{file}.md").write_text("\n".join(lines))
        print("\n".join(lines[1:-2]), "\n")
