# Adaptive Growth Workflow

Use this reference for `/profile`, `/gap`, `/roadmap`, `/weekly`, and `/monthly`.

## First setup

1. Initialize global and project state only with user opt-in.
2. If V2 files exist, follow `profile-and-sync.md`; do not delete them.
3. Run `/profile` to establish a conservative baseline.
4. Run `/gap` and then `/roadmap` only when the user wants a learning plan.

An empty profile means `Unknown`, not `Beginner`.

## During normal work

Use this lightweight loop:

```text
real task
→ A/B/C routing
→ implementation
→ diff and verification
→ one useful check or lesson
→ evidence only if meaningful
```

Do not update profiles after routine AI-owned work.

## `/profile`

Read relevant global and project evidence, then update only areas with changed evidence.

For each changed capability report:

- previous level/confidence;
- new level/confidence;
- strongest evidence;
- ownership (`User`, `Shared`, `AI`);
- why the change is justified;
- next proof.

Write project-specific details to `PROJECT_EVIDENCE.md`. Promote only a generalized statement to `EVIDENCE_LEDGER.md`.

If there is not enough evidence, keep the level and say what remains unknown.

## `/gap`

Rank at most five gaps using:

```text
priority ≈ frequency × production risk × career value × current weakness × practice availability
```

Qualitative ranking is sufficient. Prefer gaps that recur in real work and can be practiced in current projects.

For each gap include:

1. why it matters now;
2. supporting evidence;
3. what "good enough" looks like;
4. one real-work practice opportunity;
5. proof required to close or downgrade the gap.

Do not build a fashionable technology curriculum.

## `/roadmap`

Create a 4–12 week plan using at most two themes.

Each week needs:

- one real-work behavior or deliverable;
- one bounded concept;
- one observable proof;
- a fallback mini exercise if the project does not present the opportunity.

Do not prescribe long courses when the concept can be practiced in current code.

## `/weekly`

Summarize:

- meaningful work completed;
- defects or risks the user found;
- concepts newly understood or applied;
- repeated weakness patterns;
- movement in AI/user ownership;
- one or two next-week proof targets.

Do not change global levels from a weekly summary alone unless it contains strong inspectable evidence.

## `/monthly`

Optionally collect evidence first:

```bash
python <skill>/scripts/collect_monthly_context.py --month YYYY-MM
```

Then create `.ai-mentor/reports/YYYY-MM.md` using `templates/MONTHLY_REPORT.md`.

Required analysis:

1. meaningful systems or problems touched;
2. strongest user-owned evidence;
3. bugs and risk patterns;
4. capability areas whose evidence changed;
5. work transferred from AI to the user;
6. repeated weaknesses;
7. one or two next-month themes;
8. exact future proof needed for promotion.

Update the global profile only when allowed and justified. Write a generalized global report under the global `reports/` directory only when requested.

## Promotion example

Weak:

> Used transactions in three AI-generated changes, so level increases.

Strong:

> The user explained the boundary, found a partial-write defect, added a rollback regression test, and later applied the pattern with limited help.

The second example may justify `Applies` or `Reviews/Diagnoses`, depending on repetition and independence.

## AI dependency

Track ownership separately from capability:

- `0 Opaque` — AI output is not understood.
- `1 Purpose` — user understands the broad purpose.
- `2 Flow` — user can trace main execution/data flow.
- `3 Ordinary review` — user can review common logic and obvious failures.
- `4 Design and diagnosis` — user guides important design and catches subtle defects.
- `5 Engineering ownership` — user owns requirements, risk, and verification while AI implements much of the code.

AI writing many lines is compatible with level 5. The key is who owns judgment and acceptance.
