#!/usr/bin/env python3
"""Initialize global and/or project mentor state without overwriting files."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Tuple


SKILL_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = SKILL_ROOT / "templates"

GLOBAL_FILES = {
    "GLOBAL_PROFILE.md": "GLOBAL_PROFILE.md",
    "GLOBAL_SKILL_MATRIX.md": "GLOBAL_SKILL_MATRIX.md",
    "GLOBAL_SETTINGS.md": "GLOBAL_SETTINGS.md",
    "CAREER_ROADMAP.md": "CAREER_ROADMAP.md",
    "EVIDENCE_LEDGER.md": "EVIDENCE_LEDGER.md",
}

PROJECT_FILES = {
    "MENTOR_CONFIG.md": "MENTOR_CONFIG.md",
    "PROJECT_MAP.md": "PROJECT_MAP.md",
    "PROJECT_PROFILE.md": "PROJECT_PROFILE.md",
    "PROJECT_EVIDENCE.md": "PROJECT_EVIDENCE.md",
    "LEARNING.md": "LEARNING.md",
    "TECH_DEBT.md": "TECH_DEBT.md",
}


def resolve_global_dir(value: Optional[str]) -> Path:
    if value:
        return Path(value).expanduser().resolve()
    configured = os.environ.get("AI_MENTOR_HOME")
    if configured:
        return Path(configured).expanduser().resolve()
    return (Path.home() / ".ai-coding-mentor").resolve()


def copy_new(
    mappings: dict[str, str],
    destination: Path,
    mentor_level: int,
) -> Tuple[List[Path], List[Path]]:
    created: List[Path] = []
    skipped: List[Path] = []
    destination.mkdir(parents=True, exist_ok=True)

    for template_name, target_name in mappings.items():
        source = TEMPLATES / template_name
        target = destination / target_name
        if target.exists():
            skipped.append(target)
            continue

        if template_name in {"MENTOR_CONFIG.md", "GLOBAL_SETTINGS.md"}:
            content = source.read_text(encoding="utf-8")
            content = content.replace(
                "Default mentor level: `L1`",
                f"Default mentor level: `L{mentor_level}`",
                1,
            )
            target.write_text(content, encoding="utf-8")
        else:
            shutil.copy2(source, target)
        created.append(target)

    return created, skipped


def display_paths(paths: Iterable[Path]) -> None:
    for path in paths:
        print(f"  {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize AI Coding Mentor state without overwriting data."
    )
    parser.add_argument(
        "--scope",
        choices=("all", "global", "project"),
        default="all",
        help="State to initialize (default: all).",
    )
    parser.add_argument(
        "--project-dir",
        default=str(Path.cwd()),
        help="Target repository root (default: current directory).",
    )
    parser.add_argument(
        "--global-dir",
        help="Override AI_MENTOR_HOME/default user profile directory.",
    )
    parser.add_argument(
        "--mentor-level",
        type=int,
        choices=range(0, 5),
        default=1,
        metavar="0-4",
        help="Initial default intervention level (default: 1).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_dir).expanduser().resolve()
    global_root = resolve_global_dir(args.global_dir)
    created: List[Path] = []
    skipped: List[Path] = []

    try:
        if args.scope in {"all", "global"}:
            new, old = copy_new(GLOBAL_FILES, global_root, args.mentor_level)
            created.extend(new)
            skipped.extend(old)
            (global_root / "imports").mkdir(parents=True, exist_ok=True)
            (global_root / "reports").mkdir(parents=True, exist_ok=True)

        if args.scope in {"all", "project"}:
            mentor_root = project_root / ".ai-mentor"
            new, old = copy_new(PROJECT_FILES, mentor_root, args.mentor_level)
            created.extend(new)
            skipped.extend(old)
            (mentor_root / "bugs").mkdir(parents=True, exist_ok=True)
            (mentor_root / "reports").mkdir(parents=True, exist_ok=True)

            bug_template = mentor_root / "bugs" / "BUG_TEMPLATE.md"
            if bug_template.exists():
                skipped.append(bug_template)
            else:
                shutil.copy2(TEMPLATES / "BUG_TEMPLATE.md", bug_template)
                created.append(bug_template)

            adr_root = project_root / "docs" / "adr"
            adr_root.mkdir(parents=True, exist_ok=True)
            adr_template = adr_root / "ADR_TEMPLATE.md"
            if adr_template.exists():
                skipped.append(adr_template)
            else:
                shutil.copy2(TEMPLATES / "ADR_TEMPLATE.md", adr_template)
                created.append(adr_template)

            legacy = [
                mentor_root / "CAPABILITY_PROFILE.md",
                mentor_root / "SKILL_MATRIX.md",
            ]
            detected = [path for path in legacy if path.exists()]
            if detected:
                print("Legacy V2 state detected and preserved:")
                display_paths(detected)
                print("Review it during the first /profile; no scores were auto-promoted.")

    except (OSError, UnicodeError) as exc:
        print(f"Initialization failed: {exc}", file=sys.stderr)
        return 1

    print("Created:")
    display_paths(created)
    print("Skipped existing:")
    display_paths(skipped)
    print(f"Global profile directory: {global_root}")
    print(f"Project directory: {project_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
