# New member + new episode, follow-up questions, home care

**User** (Mon 26 Oct, 09:00): My son Aarav has had a fever since last night

> `ask` · member=`aarav` · episode=`e1` · reasons: age; severity; danger_signs

**Assistant:** How high has Aarav’s temperature been and is he having any other symptoms such as cough, vomiting, rash, or unusual sleepiness?

To be safe, please also tell me: is there any trouble breathing, chest pain, confusion, fainting, a seizure or unusual drowsiness?

**User** (Mon 26 Oct, 09:05): He's 6. It was 100.4F this morning, he's still playing and eating, just a bit tired. None of those.

> `home` · member=`aarav` · episode=`e1`

**Assistant:** - Offer plenty of fluids (water, milk, oral rehydration) and check that he’s peeing regularly and has moist lips and tongue.
- You can use age- and weight-appropriate paracetamol/acetaminophen for comfort if needed; avoid aspirin in children.
- Dress him in light clothing and keep the room comfortably cool rather than trying to “sweat out” the fever.
- Check his temperature every 4–6 hours and watch for new symptoms like cough, rash, vomiting, worsening tiredness, or breathing changes.
- If the fever lasts more than 2–3 days, gets higher, or he starts to look more unwell or less responsive, he should be seen by a doctor.

If anything new or worrying appears, or it isn't improving, message me again or see a doctor.

<details><summary>Memory after this scenario</summary>

```json
{
 "members": {
  "aarav": {
   "age": 6.0,
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
  }
 ]
}
```
</details>
