#!/usr/bin/env python3
"""Collect inspectable monthly evidence without assigning capability scores."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


MONTH_PATTERN = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")


def resolve_global_dir(value: Optional[str]) -> Path:
    if value:
        return Path(value).expanduser().resolve()
    configured = os.environ.get("AI_MENTOR_HOME")
    if configured:
        return Path(configured).expanduser().resolve()
    return (Path.home() / ".ai-coding-mentor").resolve()


def run_git(project: Path, args: list[str]) -> str:
    try:
        return subprocess.check_output(
            ["git", *args],
            cwd=project,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
            errors="replace",
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def read_text(path: Path, fallback: str) -> str:
    if not path.is_file():
        return fallback
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return f"Unable to read {path.name}."


def dated_markdown(directory: Path, month: str) -> str:
    if not directory.is_dir():
        return ""
    sections = []
    for path in sorted(directory.glob("*.md")):
        if path.name.endswith("_TEMPLATE.md") or "TEMPLATE" in path.name:
            continue
        text = read_text(path, "")
        if path.name.startswith(month) or month in text:
            sections.append(f"### {path.name}\n\n{text}")
    return "\n\n".join(sections)


def next_month(month: str) -> str:
    year, number = (int(part) for part in month.split("-"))
    if number == 12:
        return f"{year + 1}-01-01"
    return f"{year}-{number + 1:02d}-01"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect monthly mentor evidence; does not score skills."
    )
    parser.add_argument("--month", help="YYYY-MM; defaults to current month.")
    parser.add_argument(
        "--project-dir",
        default=str(Path.cwd()),
        help="Repository root (default: current directory).",
    )
    parser.add_argument("--global-dir", help="Override global profile directory.")
    parser.add_argument("--output", help="Optional output Markdown path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    month = args.month or datetime.now().strftime("%Y-%m")
    if not MONTH_PATTERN.fullmatch(month):
        print("Invalid --month; expected YYYY-MM.", file=sys.stderr)
        return 2

    project = Path(args.project_dir).expanduser().resolve()
    mentor = project / ".ai-mentor"
    global_root = resolve_global_dir(args.global_dir)
    start = f"{month}-01"
    end = next_month(month)

    git_log = run_git(
        project,
        [
            "log",
            f"--since={start}",
            f"--before={end}",
            "--date=short",
            "--pretty=format:%h | %ad | %s",
        ],
    )
    git_stat = run_git(
        project,
        ["log", f"--since={start}", f"--before={end}", "--shortstat", "--pretty=format:"],
    )

    bug_records = dated_markdown(mentor / "bugs", month)
    adr_records = dated_markdown(project / "docs" / "adr", month)

    legacy_parts = []
    for name in ("CAPABILITY_PROFILE.md", "SKILL_MATRIX.md"):
        path = mentor / name
        if path.is_file():
            legacy_parts.append(f"### {name}\n\n{read_text(path, '')}")

    content = f"""# Monthly Evidence Context — {month}

> Evidence collection only. This file does not assign or promote capability levels.
> Source code diffs and sensitive payloads are intentionally excluded by default.

## Git Commits

```text
{git_log or "No Git commit evidence found."}
```

## Git Change Summary

```text
{git_stat or "No Git change summary found."}
```

## Project Mentor Config

{read_text(mentor / "MENTOR_CONFIG.md", "No MENTOR_CONFIG.md found.")}

## Project Profile

{read_text(mentor / "PROJECT_PROFILE.md", "No PROJECT_PROFILE.md found.")}

## Project Evidence

{read_text(mentor / "PROJECT_EVIDENCE.md", "No PROJECT_EVIDENCE.md found.")}

## Learning Log

{read_text(mentor / "LEARNING.md", "No LEARNING.md found.")}

## Technical Debt

{read_text(mentor / "TECH_DEBT.md", "No TECH_DEBT.md found.")}

## Bugs Recorded This Month

{bug_records or "No monthly bug records found."}

## ADRs Recorded This Month

{adr_records or "No monthly ADR records found."}

## Global Profile Snapshot

{read_text(global_root / "GLOBAL_PROFILE.md", "No GLOBAL_PROFILE.md found or accessible.")}

## Global Skill Matrix Snapshot

{read_text(global_root / "GLOBAL_SKILL_MATRIX.md", "No GLOBAL_SKILL_MATRIX.md found or accessible.")}

## Global Evidence Ledger Snapshot

{read_text(global_root / "EVIDENCE_LEDGER.md", "No EVIDENCE_LEDGER.md found or accessible.")}

## Legacy V2 Project Evidence

{chr(10).join(legacy_parts) if legacy_parts else "No legacy V2 profile files found."}
"""

    output = (
        Path(args.output).expanduser().resolve()
        if args.output
        else mentor / "reports" / f"{month}-evidence.md"
    )
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")
    except OSError as exc:
        print(f"Unable to write evidence file: {exc}", file=sys.stderr)
        return 1

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
