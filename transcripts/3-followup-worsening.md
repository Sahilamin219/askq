# Implicit member via open episode, update attaches to it, worsening -> doctor

**User** (Thu 29 Oct, 09:00): His fever is still there, it touched 102.5 last night and he's eating less

> `doctor` · member=`aarav` · episode=`e1` · reasons: fever for 3+ days; getting worse; assistant judged a doctor is needed

**Assistant:** This needs a doctor's review. I'm transferring this case to a human doctor, who will contact you shortly. If things get worse before then, call 112.

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
   "updated": "2026-10-29T09:00",
   "onset": "2026-10-25T09:00",
   "symptoms": [
    "fever",
    "tiredness",
    "reduced appetite"
   ],
   "severity": "moderate",
   "trend": "worse",
   "screen": "done",
   "red_flags": [],
   "questions": 1,
   "disposition": "doctor"
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
