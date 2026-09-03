# Capability Assessment Guide

Use this reference for `/profile`, `/gap`, `/roadmap`, and `/monthly`.

## Assess behavior, not exposure

Weak evidence:

- the repository contains a technology;
- AI generated the implementation;
- a ticket was closed;
- the user read an explanation;
- tests passed but the user did not inspect or design them.

Stronger evidence:

- user explains the current execution and failure flow correctly;
- user predicts a failure or race condition;
- user finds a real defect in AI output;
- user creates a meaningful regression test;
- user implements a related pattern with limited help;
- user selects a simpler design and explains the tradeoff;
- user diagnoses a production issue and verifies the fix.

## Capability levels

### 0 — Unknown

No useful evidence. Do not interpret this as inability.

### 1 — Recognizes

Can identify purpose and follow an explanation.

### 2 — Understands

Can explain ordinary behavior, trace the flow, and identify common failures.

### 3 — Applies

Can perform ordinary real tasks with limited guidance and design relevant tests.

### 4 — Reviews / Diagnoses

Can find mistakes, diagnose failures, compare tradeoffs, and reject unnecessary complexity.

### 5 — Owns / Teaches

Can make reliable design decisions, define verification, guide AI or people, and repeatedly prevent defects.

## Confidence

- **High:** several strong evidence points across different tasks or projects.
- **Medium:** at least one strong or several moderate evidence points.
- **Low:** sparse, indirect, conflicting, or stale evidence.

Level and confidence are independent. A high level with low confidence means promising but insufficiently repeated evidence.

## Evidence strength

Prefer:

1. production/debugging evidence;
2. a defect found during review;
3. independent design or implementation;
4. a regression test;
5. a correct explanation or `/check`;
6. repeated guided work;
7. exposure.

Record ownership:

- **User:** user made the judgment or implementation with minimal help.
- **Shared:** AI and user materially collaborated.
- **AI:** AI made the decision or implementation; useful only as exposure unless the user later demonstrates understanding.

## Global versus project evidence

Global evidence must demonstrate a transferable concept and omit sensitive detail. Project evidence can establish familiarity with local architecture or conventions without proving broad mastery.

Do not average project scores. Resolve evidence by strength, recency, repetition, and independence.

## Promotion guardrails

- Do not promote from one weak signal.
- Require application, diagnosis, or repeated explanation to move beyond level 2.
- Require repeated cross-context evidence for high-confidence levels 4–5.
- Do not demote because one answer was wrong; lower confidence or set a new proof target first.
- Reassess stale capabilities when the underlying technology or evidence is old.

## Gap prioritization

Prefer gaps that are frequent, risky, career-relevant, repeatedly weak, and trainable through current work.

For work-first mentoring, prioritize C-class judgment gaps over typing speed or memorizing routine syntax.
