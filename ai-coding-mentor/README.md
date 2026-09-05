# AI Coding Mentor

**Work-First Adaptive Mentor** for engineers who use AI to deliver real software but want to retain understanding, review judgment, and architecture ownership.

The skill defaults to roughly **85% delivery / 15% learning** through `/normal` + `L1`. It does not turn every implementation into a lesson.

## What this skill changes

- Separates the reusable Skill from the engineer's persistent profile.
- Uses one global profile across local CLIs and a separate context profile per repository.
- Routes work into A (AI executes), B (AI executes + summarizes), and C (user judgment matters).
- Adds intervention levels `L0–L4` so urgency and learning depth are explicit.
- Limits normal-mode active learning to one high-value concept.
- Treats missing profile data as unknown, not beginner-level ability.
- Records whether evidence was user-owned, shared, or AI-owned.
- Preserves V2 profile files and migrates them conservatively.
- Excludes proprietary project detail from the global profile.
- Supports safe profile export/import without overwriting live state.
- Keeps evidence-based review, verification, Bug DB, ADRs, technical debt, `/check`, `/weekly`, and `/monthly`.
- Exports evidence-based daily, weekly, and monthly learning reports as Markdown, standalone HTML, Word, PDF, or all four formats.

## How it decides what to teach

| Class | Typical work | Default L1 behavior |
|---|---|---|
| A | Boilerplate, repetitive CRUD, mapping, mechanical edits | AI completes it. |
| B | Ordinary service logic, queries, validation, integrations | AI completes it and summarizes the important diff. |
| C | Architecture, transactions, concurrency, permissions, money, deletion, state, cache, retry, idempotency, migrations, security | Surface the most important judgment/risk and verify it carefully. |

The profile influences attention, but never overrides current requirements, safety, or authorization.

## Intervention levels

| Level | Use | Learning behavior |
|---|---|---|
| L0 | Incident or urgent delivery | No learning pause. |
| L1 | Normal work (default) | At most one active learning pause. |
| L2 | Balanced work and growth | Up to two focused decisions. |
| L3 | Growth-focused work | User predicts/designs important parts. |
| L4 | Study | User attempts first; AI reviews and fills gaps. |

Examples:

```text
Use ai-coding-mentor.
/normal
mentor_level=L1
Implement the order-cancellation endpoint and verify it.
```

```text
Use ai-coding-mentor.
/fast
Fix this production regression with the smallest safe patch.
```

```text
Use ai-coding-mentor.
/study
Let me design the transaction boundary before you implement it.
```

## Learning report exports

Markdown is the canonical source and default format. HTML, DOCX, and PDF outputs are derived from the same normalized report so evidence, ownership, conclusions, and proof targets remain consistent.

```text
Use ai-coding-mentor.
/daily format=md
```

```text
Use ai-coding-mentor.
/weekly format=html week=2026-W36
```

```text
Use ai-coding-mentor.
/monthly format=docx,pdf month=2026-09
```

```text
Use ai-coding-mentor.
/export period=weekly date=2026-09-05 format=all scope=project
```

Exports are explicit-only by default: routine coding tasks, `/learn`, `/summary`, and profile updates do not create report files. Automatic generation happens only after the user intentionally changes `Automatic learning report exports` to `Yes` in project or global settings.

Defaults are the current local period, local timezone, project scope, and Markdown. `word` is accepted as an alias for a real `.docx` file. Exports are written under:

```text
<repo>/.ai-mentor/reports/learning/
├── daily/YYYY-MM-DD/
├── weekly/YYYY-Www/
└── monthly/YYYY-MM/
```

DOCX and PDF exports require a host with real document generation and rendering support. The skill never renames HTML or Markdown to simulate those formats. Every DOCX and PDF must be rendered to page images and inspected before it is reported as verified.

See the [learning report export guide](references/learning-export-guide.md) for evidence selection, privacy rules, filenames, collision handling, cross-format parity, and verification gates.

## Persistent state

Global engineer state:

```text
~/.ai-coding-mentor/
├── GLOBAL_PROFILE.md
├── GLOBAL_SKILL_MATRIX.md
├── GLOBAL_SETTINGS.md
├── CAREER_ROADMAP.md
├── EVIDENCE_LEDGER.md
├── imports/
└── reports/
    └── learning/
        ├── daily/
        ├── weekly/
        └── monthly/
```

Project context:

```text
<repo>/.ai-mentor/
├── MENTOR_CONFIG.md
├── PROJECT_MAP.md
├── PROJECT_PROFILE.md
├── PROJECT_EVIDENCE.md
├── LEARNING.md
├── TECH_DEBT.md
├── bugs/
└── reports/
    └── learning/
        ├── daily/
        ├── weekly/
        └── monthly/
```

Install the Skill in each compatible CLI, but point every local CLI at the same profile directory. Reinstalling the Skill does not reset the profile.

## Initialize state

Run from a repository only after opting into mentor state files:

```bash
python <skill-folder>/scripts/init_state.py --scope all
```

The script never overwrites existing files. Use `AI_MENTOR_HOME` or `--global-dir` to choose a shared global profile location.

## Monthly evidence

```bash
python <skill-folder>/scripts/collect_monthly_context.py --month 2026-09
```

The collector gathers Git summaries and mentor records but does not score capabilities or include source diffs by default.

## Move a profile between machines

```bash
python <skill-folder>/scripts/profile_portability.py export --output mentor-profile.zip
python <skill-folder>/scripts/profile_portability.py import --bundle mentor-profile.zip
```

Import stages a merge candidate under `imports/`; it never overwrites the live profile. Review it with `/profile`.

## V2 compatibility

The initializer leaves these files untouched when found:

```text
.ai-mentor/CAPABILITY_PROFILE.md
.ai-mentor/SKILL_MATRIX.md
```

On the first `/profile`, they are treated as legacy project evidence. Only generalized, evidence-backed conclusions should move into the global profile.

## Package structure

```text
ai-coding-mentor/
├── SKILL.md
├── README.md
├── INSTALL.md
├── references/
├── templates/
├── scripts/
└── tests/
```

## Goal

AI can write most of the code. The engineer still owns what the software should do, where it can fail, how it is verified, and which decisions matter.
