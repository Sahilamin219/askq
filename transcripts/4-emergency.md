# Red flags short-circuit everything: no questions, fixed emergency message

**User** (Fri 30 Oct, 09:00): My mother suddenly has a crooked face and can't lift her right arm

> `emergency` · member=`mom` · episode=`e3` · reasons: stroke_signs; keyword: crooked face

**Assistant:** This could be a medical emergency. Call 112 or go to the nearest emergency department right now. Do not wait for an online reply.

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
  },
  "mom": {
   "age": null,
   "facts": []
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
  },
  {
   "id": "e3",
   "member": "mom",
   "title": "sudden crooked face and weakness in right arm",
   "status": "open",
   "opened": "2026-10-30T09:00",
   "updated": "2026-10-30T09:00",
   "onset": "2026-10-30T09:00",
   "symptoms": [
    "sudden crooked face",
    "right arm weakness",
    "possible stroke"
   ],
   "severity": "severe",
   "trend": null,
   "screen": "todo",
   "red_flags": [
    "stroke_signs",
    "keyword: crooked face"
   ],
   "questions": 0,
   "disposition": "emergency"
  }
 ]
}
```
</details>
