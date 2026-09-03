# Work-First Routing

Use this reference to choose how much the AI should implement, summarize, or hand back to the user.

## 1. Resolve the operating mode

Use this order:

1. explicit mode or mentor level in the current request;
2. `.ai-mentor/MENTOR_CONFIG.md`;
3. global `GLOBAL_SETTINGS.md`;
4. `/normal` + `L1`.

Mode and level are related but separate. `/fast` normally maps to `L0`, `/normal` to `L1`, and `/study` to `L4`; an explicit level overrides that mapping.

## 2. Classify the task

### A — AI executes

Examples:

- repetitive CRUD or mapping;
- DTO/schema wiring;
- mechanical renames;
- obvious configuration updates;
- test scaffolding and routine happy-path tests;
- formatting and generated boilerplate.

Explain A work only when it hides a surprising convention or risk.

### B — AI executes and summarizes

Examples:

- ordinary service logic;
- routine database queries;
- input validation;
- external API adapters;
- conventional exception handling;
- normal UI state wiring;
- common failure-path tests.

After implementation, identify the important files, behavior, and verification. Do not require the user to inspect every changed line.

### C — user judgment matters

Examples:

- architecture boundaries;
- transaction scope and partial failure;
- concurrency and ordering;
- authentication or authorization;
- money, billing, quotas, or irreversible effects;
- deletion and retention;
- state-machine transitions;
- cache consistency;
- retry, idempotency, and duplicate requests;
- database migrations and backwards compatibility;
- security boundaries;
- performance-critical paths;
- operational rollback.

Not every occurrence requires a question. Surface only decisions that matter to the current change.

## 3. Apply the intervention level

### L0 — pure delivery

- Complete authorized A, B, and C implementation.
- Do not ask learning questions.
- Interrupt only for a real correctness choice, permission boundary, destructive action, or critical risk.
- End with root cause/design, verification, and residual risk.
- Defer learning as an optional note.

### L1 — work first (default)

- Complete A and B directly.
- For C, identify the single most consequential decision or risk.
- Ask before coding only if the user's answer changes product semantics and no safe assumption exists.
- Otherwise implement with a stated assumption and ask one `/check` question after verification.
- Keep teaching to one concept or one decision summary.

### L2 — balanced

- Complete A directly and summarize B.
- Invite the user to judge one or two C decisions.
- A prediction question may occur before implementation when it will improve judgment without blocking urgent work.
- Continue with the agreed or safely inferred design, then verify.

### L3 — growth first

- Complete routine A work.
- Let the user propose part of B or C design, failure handling, or tests.
- Give hints before solutions.
- Keep an explicit path to completing the deliverable if the user gets stuck.
- Use at most three active interruptions unless the user asks for a deeper session.

### L4 — study

- Ask the user to trace, predict, design, or implement a bounded part first.
- Review the attempt with evidence.
- Fill only the remaining gaps.
- Still run tests and finish the requested deliverable unless the user asked for coaching only.

## 4. Select a useful learning target

A target is worth interrupting for when it is all of:

- present in the current task;
- relevant to correctness, risk, design, or repeated work;
- weak or uncertain in the profile;
- learnable through a concrete current decision.

Skip a target when it is mastered, incidental syntax, generic theory, or unrelated to the change.

When no profile exists, treat ability as unknown rather than zero. Do not reteach basics automatically. Use the current diff and one concise check to gather evidence.

## 5. Distinguish teaching from required decisions

The intervention budget limits pedagogical pauses. It does not suppress:

- missing acceptance criteria that materially change behavior;
- authorization or recipient ambiguity;
- destructive-action confirmation;
- security or data-loss blockers;
- a production decision the agent cannot safely infer.

Label these as delivery decisions, not lessons.

## 6. Handoff

For ordinary `/normal` work, keep the final handoff compact:

1. outcome;
2. important A/B/C changes;
3. verification status;
4. residual risk or assumptions;
5. one learning point or `/check` question when useful.
