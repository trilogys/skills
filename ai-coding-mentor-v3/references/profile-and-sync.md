# Profile and Sync Guide

Use this reference when initializing, reading, updating, migrating, exporting, importing, or synchronizing mentor state.

## State model

### Global engineer profile

Default location:

```text
~/.ai-coding-mentor/
```

Override only with:

```text
AI_MENTOR_HOME
```

This layer stores generalized capability, evidence, preferences, and career direction. It must not depend on one repository.

### Project context profile

Location:

```text
<repo>/.ai-mentor/
```

This layer stores architecture, project vocabulary, local learning examples, bugs, technical debt, and project-specific evidence.

### Decision rule

Use global capability for transferable concepts. Use project evidence for familiarity with this codebase and domain.

Example:

- Global: transactions `Level 3`.
- Project: unfamiliar unit-of-work wrapper and event-outbox convention.
- Adaptation: do not reteach ACID basics; explain only this project's boundary and convention.

## Reading order

For non-trivial work, read only files that exist and are relevant:

1. project `MENTOR_CONFIG.md`;
2. global `GLOBAL_SETTINGS.md`;
3. global `GLOBAL_PROFILE.md` and `GLOBAL_SKILL_MATRIX.md`;
4. project `PROJECT_PROFILE.md`, `PROJECT_MAP.md`, and recent evidence related to the task.

Do not load entire histories when a targeted search is enough.

## Initialization

Run from the target repository:

```bash
python <skill>/scripts/init_state.py --scope all
```

The initializer never overwrites existing files. `--scope project` creates only repository state; `--scope global` creates only user state. Use `--global-dir` when a CLI cannot resolve the intended home directory.

Initialization is an opt-in write. Do not run it merely because the skill was invoked.

## V2 migration

V2 may contain:

```text
.ai-mentor/CAPABILITY_PROFILE.md
.ai-mentor/SKILL_MATRIX.md
```

Treat these as legacy project evidence.

Rules:

1. never delete, rename, or overwrite them automatically;
2. initialize the V3 files alongside them;
3. read the legacy files on the first `/profile`;
4. preserve supported levels but reassess confidence and ownership;
5. copy only generalized, non-sensitive conclusions into global state;
6. record the migration source in `EVIDENCE_LEDGER.md` without proprietary detail.

This preserves learning without pretending all project exposure proves global mastery.

## Profile update policy

Update a profile only when evidence changes.

For each signal record:

- date;
- capability;
- evidence type;
- ownership: `User`, `Shared`, or `AI`;
- outcome;
- confidence;
- next proof.

Do not increase a level from one weak signal. A failed check can lower confidence without automatically lowering level. Repeated inability to apply a concept may justify a level review.

## Permission boundary

Project files are part of the repository and may affect Git status. Global files live outside it.

- Read existing global state when filesystem access permits.
- Write project evidence only after state has been initialized or the user explicitly requests it.
- Write global state only when explicitly requested by `/profile` or `/monthly`, or when existing settings opt into updates.
- Do not silently enable auto-updates.

If writes are unavailable, provide the proposed evidence entry in the handoff instead of claiming it was saved.

## Privacy boundary

Global state may be read from many projects and synchronized between machines. Keep it generalized.

Never promote:

- secrets, tokens, or credentials;
- source code or diffs;
- customer/user names;
- proprietary repository paths;
- incident payloads or database rows;
- confidential product plans;
- internal hostnames or endpoints.

Use a neutral project alias only when distinguishing evidence sources is necessary.

Project state can contain local file references but must still exclude secrets and sensitive payloads.

## Same-machine cross-CLI continuity

All local CLIs can share the same profile if they can access the same global directory. Installing the skill in several CLIs does not duplicate the profile; the skill and profile are separate.

If a sandbox or remote session cannot access the local user home, it cannot see the local profile. In that case use repository state or mount/sync the global state explicitly. State the limitation.

## Multi-machine continuity

Choose one controlled mechanism:

- a private Git repository containing only generalized global files;
- an encrypted/synchronized private folder;
- `scripts/profile_portability.py export` and `import`.

Do not place global or project profiles in a public repository by default.

The portability importer stages files under `imports/`; it does not overwrite the live profile. Run `/profile` to compare and merge. Resolve conflicts by evidence date and strength, not by blindly selecting the newest file.

## Git recommendations

Project state has mixed sensitivity:

- usually commit `PROJECT_MAP.md`, selected ADRs, and non-personal `TECH_DEBT.md` when useful to the team;
- usually keep personal capability evidence, learning notes, and reports private or ignored;
- follow employer and repository policy before committing any mentor state.

The skill must not modify `.gitignore` without the user's request.

## Failure behavior

- Missing global profile: use `Unknown`; do not invent levels.
- Stale profile: lower confidence or request fresh proof.
- Conflicting evidence: preserve both signals and explain the conflict.
- Corrupt/malformed file: do not overwrite it; make a backup or ask before repair.
- Concurrent edits: stop before overwriting and merge explicitly.
