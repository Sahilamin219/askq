# Switching member, long-term memory, deterministic doctor handoff, general query

**User** (Mon 26 Oct, 09:00): Papa is 68 and has type 2 diabetes. Since yesterday he's had burning when he urinates.

> `ask` · member=`papa` · episode=`e2` · reasons: severity; danger_signs

**Assistant:** Has Papa also noticed needing to pee more often, blood in the urine, fever, or pain in his lower belly or back?

To be safe, please also tell me: is there any trouble breathing, chest pain, confusion, fainting, a seizure or unusual drowsiness?

**User** (Mon 26 Oct, 09:05): It's moderate, no fever or back pain. No to all of those, he's alert.

> `doctor` · member=`papa` · episode=`e2` · reasons: age 65+ with known conditions; assistant judged a doctor is needed

**Assistant:** This needs a doctor's review. I'm transferring this case to a human doctor, who will contact you shortly. If things get worse before then, call 112.

**User** (Mon 26 Oct, 09:10): What should he be eating to keep his sugar in check?

> `answer` · member=`papa` · episode=`None`

**Assistant:** For Papa’s type 2 diabetes, general eating tips that are usually helpful:
- Base meals on vegetables, lentils/beans, whole grains (like brown rice, whole‑wheat roti) and lean protein; keep portions moderate.
- Limit sweets, sugary drinks (including fruit juice), white bread, white rice, and deep‑fried or very oily foods.
- Choose high‑fiber carbs (vegetables, salads, whole grains) and spread them through the day instead of one very heavy meal.
- Prefer water, unsweetened tea/coffee; avoid adding sugar; be cautious with tropical fruits and have small portions with a meal, not alone.
- Try to eat at regular times and check blood sugars as his doctor advised, noting which foods seem to raise his readings more.

<details><summary>Memory after this scenario</summary>

```json
{
 "members": {
  "aarav": {
   "age": 6.0,
   "facts": []
  },
  "papa": {
   "age": 68.0,
   "facts": [
    "type 2 diabetes"
   ]
  }
 },
 "episodes": [
  {
   "id": "e1",
   "member": "aarav",
   "title": "fever since last night",
   "status": "open",
   "opened": "2026-10-26T09:00",
   "updated": "2026-10-26T09:05",
   "onset": "2026-10-25T09:05",
   "symptoms": [
    "fever",
    "tiredness"
   ],
   "severity": "mild",
   "trend": null,
   "screen": "done",
   "red_flags": [],
   "questions": 1,
   "disposition": "home"
  },
  {
   "id": "e2",
   "member": "papa",
   "title": "burning on urination",
   "status": "open",
   "opened": "2026-10-26T09:00",
   "updated": "2026-10-26T09:05",
   "onset": "2026-10-25T09:05",
   "symptoms": [
    "painful urination"
   ],
   "severity": "moderate",
   "trend": null,
   "screen": "done",
   "red_flags": [],
   "questions": 1,
   "disposition": "doctor"
  }
 ]
}
```
</details>
