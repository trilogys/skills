# Learning Report Export Guide

Use this workflow for explicit daily, weekly, monthly, or export requests. Reporting summarizes inspectable learning evidence; it does not create new capability evidence by itself.

## Request Surface

Accept natural language or command-shaped requests such as:

```text
/daily format=md
/weekly format=html week=2026-W36
/monthly format=docx,pdf month=2026-09
/export period=weekly date=2026-09-05 format=all scope=project
```

Treat `word` as an alias for `docx`. Accept comma-separated formats. `all` means `md,html,docx,pdf`.

Defaults when omitted:

- period command determines `daily`, `weekly`, or `monthly`;
- date is the current local date;
- timezone is the user's local timezone;
- scope is `project`;
- format is `md`;
- output directory is the period directory below;
- language follows the current conversation or an explicit setting.

Do not schedule recurring exports from these commands. Scheduling is a separate user request and authorization boundary.

An explicit export request authorizes creation of the selected report directory and files only. It does not authorize full mentor-state initialization, global profile changes, `.gitignore` edits, publication, or sharing.

## Resolve The Period

- **Daily:** one local calendar day, named `YYYY-MM-DD`.
- **Weekly:** ISO week Monday through Sunday, named `YYYY-Www`. A supplied date selects the ISO week containing that date.
- **Monthly:** one local calendar month, named `YYYY-MM`.

Record the timezone and inclusive date range in the canonical report. Do not mix evidence outside the selected range. When timezone ambiguity can change inclusion, state the assumed timezone before generating.

## Evidence Inputs

Read only relevant sources that exist and are authorized:

- `.ai-mentor/LEARNING.md`;
- `.ai-mentor/PROJECT_EVIDENCE.md` and `PROJECT_PROFILE.md`;
- dated bug records and relevant ADRs;
- verification summaries and user-owned decisions from the selected period;
- Git commit metadata and change summaries, without copying source diffs by default;
- generalized global evidence only when the requested scope and permissions allow it.

Never infer learning from commit volume, changed-line count, time spent, dependencies used, AI-authored code, or a report generated in an earlier period. If evidence is absent or weak, say so.

Before export, remove secrets, credentials, customer identities, proprietary hostnames, incident payloads, source code, confidential plans, and unnecessary local paths. Project reports may name local modules when useful but must still exclude sensitive payloads. Global reports contain generalized evidence only.

## Canonical Markdown First

Create one normalized Markdown report before any other format. Use:

- [daily template](../templates/DAILY_LEARNING_REPORT.md) for daily reports;
- [weekly template](../templates/WEEKLY_LEARNING_REPORT.md) for weekly reports;
- [monthly template](../templates/MONTHLY_REPORT.md) for monthly reports.

Every report includes:

- report ID, period, timezone, scope, and evidence cutoff;
- meaningful work and verified outcomes;
- evidence with `User`, `Shared`, or `AI` ownership;
- lessons and recognition patterns;
- defects, risks, uncertainty, and missing evidence;
- ownership movement when supported;
- one or two next proof targets;
- verification status.

Normalize line endings to LF, remove the `Canonical SHA-256:` metadata line, and calculate SHA-256 over the remaining final UTF-8 Markdown bytes. Write that hash into the canonical metadata and every derived format. This avoids a self-referential hash while letting the user identify the exact canonical content.

## Output Locations And Names

Project scope:

```text
<repo>/.ai-mentor/reports/learning/
├── daily/YYYY-MM-DD/learning-daily-YYYY-MM-DD.<ext>
├── weekly/YYYY-Www/learning-weekly-YYYY-Www.<ext>
└── monthly/YYYY-MM/learning-monthly-YYYY-MM.<ext>
```

Global scope, only when explicitly requested:

```text
<AI_MENTOR_HOME>/reports/learning/<period>/<period-id>/learning-<period>-<period-id>.<ext>
```

Create only requested formats. Do not modify `.gitignore`. Warn that project reports may appear in Git status and may contain personal learning evidence. The report directory may be created even when the rest of `.ai-mentor/` has not been initialized.

If a target already exists, compare it first. Replace it only when the user explicitly asked to update or regenerate that period. Otherwise add a timestamp suffix and preserve the existing report.

## Format Pipelines

### Markdown

- Write UTF-8 Markdown using the canonical template.
- Keep headings, tables, links, code, and evidence ownership readable in plain text.
- Validate that required sections exist and the file reopens as UTF-8.

### HTML

- Render the canonical content into one standalone semantic HTML file with embedded CSS and no required JavaScript or external assets.
- Include `lang`, UTF-8 metadata, one `main`, logical headings, accessible tables, visible links, and print CSS.
- Use a restrained report layout, readable line length, page-safe spacing, and black text that prints clearly.
- Open the final HTML in a browser at a normal desktop viewport and inspect print behavior. Check long links, code blocks, tables, and page breaks.

### Word

- Produce a real `.docx`, never renamed HTML, RTF, Markdown, or plain text.
- Use the host's dedicated document capability when available. Preserve the canonical section order and evidence tables.
- Use a plain descriptive Word title without decorative punctuation. Keep styling professional and restrained.
- Scrub unintended author, revision, and custom metadata when the report may be shared.
- Render the final DOCX to PNG pages, inspect every page at 100% zoom, fix defects, and render again. Validate no clipping, missing glyphs, broken tables, or bad page breaks.

### PDF

- Produce a real PDF through the host's PDF capability or a known renderer.
- When DOCX and PDF are both requested and the document renderer can emit PDF from the verified DOCX, prefer that path to keep pagination and styling aligned.
- Otherwise create the PDF from the canonical report or verified standalone HTML without changing content.
- Reopen the PDF, confirm it is non-empty and structurally readable, render every page to PNG, and visually inspect the result.

## Cross-Format Parity

Derived formats may adapt layout but not meaning. Require all requested formats to share:

- report ID, period, timezone, scope, and canonical hash;
- section order and headings;
- evidence rows and ownership labels;
- capability conclusions and confidence limits;
- next proof targets and verification status.

After generation, extract or inspect enough text from DOCX and PDF to compare these invariants with the canonical Markdown. Do not accept visual similarity as proof of content parity.

## Failure And Partial Completion

- Missing DOCX/PDF tooling: produce requested Markdown/HTML formats that can be verified, then name the missing capability and leave unsupported formats uncreated.
- Render failure: diagnose once using the available logs and retry after a concrete fix. Do not deliver an unrendered DOCX or PDF as verified.
- Missing evidence: create a short honest report with gaps and next evidence needed; do not fabricate content.
- Corrupt existing target: do not overwrite it. Preserve it and use a new filename or ask before repair.
- Write restriction: return the normalized report in chat only if useful and state that no file was saved.

## Completion Report

State:

- selected period and timezone;
- evidence sources used and important gaps;
- output scope and directory;
- each requested file and its verification status;
- any format not created and the exact reason.

Use `Verified`, `Partially verified`, or `Not verified - reasoning only` consistently with the main skill.
