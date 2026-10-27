# Family Health AI Agent Loop — Assignment brief (input, verbatim)

## 1. Overview
Design and implement a lightweight, extensible agentic loop for a long-term family health
assistant. The system processes everyday health queries, triages active symptoms, maintains
historical context across multiple individuals, and enforces strict escalation boundaries when
clinical handoff is warranted.

## 2. Context & Objectives
In a multi-user household, health conversations are fluid. A single user profile may query about
different dependents across varying timelines (e.g., an acute fever for a child versus a chronic
condition for an elderly parent).
Your objective is to orchestrate an end-to-end processing pipeline that balances probabilistic
LLM reasoning (empathy, information gathering, intent extraction) with deterministic
programmatic guardrails (safety rules, routing logic, fixed escalation responses).

## 3. Scope Boundaries
- **In Scope:** General health inquiries, symptom intake, progressive clinical follow-ups,
  contextual entity/episode resolution, and escalation triggers.
- **Out of Scope (Design for Extensibility):** Automated lab report analysis, custom
  knowledge base, or live third-party telemedicine integrations. The codebase should
  provide clear extension points so these capabilities can be plugged in.

## 4. Functional Requirements

### A. Implicit Member & Episode Disambiguation
- Infer which family member a query pertains to without forcing explicit identification on
  every turn.
- Identify and maintain distinct episodes. The system should automatically associate
  follow-up updates with an active episode, opening new episodes for new conditions.

### B. Symptom Triaging & Context Gathering
- Dynamically assess user-reported symptoms.
- Formulate focused, clinical follow-up questions to gather missing triage parameters (e.g.,
  duration, severity, red-flag symptoms, associated factors) before concluding an
  assessment.
- The system should be able to manage memories and states across users and their
  episodes intelligently and use those memory facts in subsequent triages and query
  responses for the user.

### C. Agent assessment and escalation scenarios
- The harness should detect any critical emergency red flags and indicate that to the user
  to take an action with the local emergency services.
- When the harness judges that this is not critical but still needs doctor review, the system
  must indicate that to the user by returning a predetermined, deterministic message
  informing the user that the case is being transferred to a human doctor. You do not need
  to build the doctor dashboard or routing logic.
- The system can also decide that the situation is not critical, nor does it require a doctor's
  review, and can suggest home monitoring steps to the user.

## 5. Constraints & Deliverables
1. **Code Repository:** Don't treat this as a production-grade harness. It exists only so we can
   evaluate this assignment. Write only the code needed to meet the requirements above.
   Among submissions that meet them, we will favour the one that does so in the fewest
   lines of code.
2. **Future Product spec:** Use this document as a scratch pad for your vision of the product.
   Briefly describe what it could become and where it could be used. Keep it concise, but
   feel free to be imaginative about the north star product you have in mind.
3. **Scenario test runs:** Run 3 to 4 scenarios against your harness locally and include the
   transcripts. Do not include more than four. Choose them to be as diverse as possible, so
   that together they cover the harness's most important behaviours.
4. **Readme:** A short write-up explaining your approach and design decisions you took.
