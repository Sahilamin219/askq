# Family Health Agent Loop

One household account, many family members, many illness episodes over time. Each message goes through one loop:

```
message → load memory → LLM fills a structured form → code decides → reply → save memory
```

```bash
export OPENAI_API_KEY=...
uv run agent.py               # chat in the terminal; memory persists in memory.json
uv run scenarios.py           # runs the 4 scenarios and writes transcripts/
```

## Approach: the LLM understands, code decides

**One LLM call per turn** (`understand`). The model gets the household memory (members, open episodes, recent turns) and fills
a typed `Understanding` form through strict structured output (OpenAI; one function to swap providers). That form holds who the message is about, which episode, symptoms,
duration, severity, red flags (from a closed list), trend, its own level of concern, one follow-up question and advice.
It never chooses the outcome.

**Deterministic decision ladder** (`step`), in this order:

1. **Emergency.** Any listed red flag (from the LLM, or a negation-aware keyword backstop on the raw text) → fixed emergency message. This is checked before anything else, so no questions are asked first.
2. **Clarify who.** A symptom with no resolvable member → ask. We never guess, because a wrong guess would apply one person's history to someone else.
3. **Gather.** Until age, duration, severity and a danger-sign check are known, send the LLM's follow-up question. The danger-sign checklist itself is fixed text asked by code: in the first run the LLM marked "screened" just because a parent said "he's playing", so safety screening is no longer the model's call. The budget is 3 questions per episode, so it never turns into an interrogation.
4. **Doctor.** Fixed rules (infant, 65+ with conditions, severe, fever 3+ days, 7+ days, worsening, triage still incomplete after the budget, or the LLM's own concern) → fixed handoff message.
5. **Home care.** The LLM's tailored advice plus a fixed safety-net line.

The LLM's `concern` can only **raise** the outcome. A rule can never be talked down by the model.

## Design decisions

- **Member and episode resolution are part of the same extraction.** Pronouns ("his fever") are resolved against open episodes, not only against the last speaker. Code then validates the result: an unknown episode id, an id from another member, or a closed episode all open a new episode.
- **Memory is split in two:** lasting member facts (age, conditions, medicines, allergies) and per-episode triage state. Both go back into every prompt, which is how "Papa is diabetic" shapes later advice and rules. Episodes close on recovery or after 14 days without updates.
- **Time is computed, not remembered.** Onset is stored as a timestamp, so "fever 3+ days" stays true on day 3 without the user restating it.
- **Missing is not negative.** Unknown fields stay `null` and count as missing. They are never treated as "no".
- **Fail safe.** If the LLM fails, the keyword check still runs and the user gets a fixed reply. The message is never dropped.
- **Extension points:** `CONTEXT_PLUGINS` (lab-report readers, knowledge-base retrieval add context) and `HANDOFF_PLUGINS` (telemedicine and doctor queues receive escalated episodes). The loop itself doesn't change.
- **Small on purpose:** a JSON file instead of a database, a terminal instead of a server, one provider. The rules and texts are module constants, so clinicians can review them in one screen.

## Known limits

- One member per message. "Both kids have a cough" gets resolved to one of them, or to a clarification question.
- Rules and red flags are illustrative, not clinically validated.
- The keyword backstop prefers false alarms: "he was unconscious last year" escalates, while "no seizure" does not.
