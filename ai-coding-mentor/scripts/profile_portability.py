#!/usr/bin/env python3
"""Export global profile state or safely stage an imported profile for review."""

from __future__ import annotations

import argparse
import json
import os
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Optional


ROOT_NAME = "ai-coding-mentor-profile"
PROFILE_FILES = (
    "GLOBAL_PROFILE.md",
    "GLOBAL_SKILL_MATRIX.md",
    "GLOBAL_SETTINGS.md",
    "CAREER_ROADMAP.md",
    "EVIDENCE_LEDGER.md",
)
MAX_ENTRY_BYTES = 5 * 1024 * 1024
MAX_TOTAL_BYTES = 20 * 1024 * 1024


def resolve_global_dir(value: Optional[str]) -> Path:
    if value:
        return Path(value).expanduser().resolve()
    configured = os.environ.get("AI_MENTOR_HOME")
    if configured:
        return Path(configured).expanduser().resolve()
    return (Path.home() / ".ai-coding-mentor").resolve()


def export_profile(global_root: Path, output: Path) -> int:
    available = [name for name in PROFILE_FILES if (global_root / name).is_file()]
    if not available:
        print("No global profile files found to export.", file=sys.stderr)
        return 1

    manifest = {
        "format": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "files": available,
        "note": "Generalized global profile only; inspect before sharing.",
    }
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(f"{ROOT_NAME}/manifest.json", json.dumps(manifest, indent=2))
            for name in available:
                archive.write(global_root / name, f"{ROOT_NAME}/{name}")
    except OSError as exc:
        print(f"Export failed: {exc}", file=sys.stderr)
        return 1

    print(output)
    return 0


def safe_entries(archive: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
    allowed = {f"{ROOT_NAME}/{name}" for name in PROFILE_FILES}
    allowed.add(f"{ROOT_NAME}/manifest.json")
    entries = archive.infolist()
    total = 0
    for info in entries:
        path = PurePosixPath(info.filename)
        if info.is_dir():
            continue
        if path.is_absolute() or ".." in path.parts or info.filename not in allowed:
            raise ValueError(f"Unexpected archive entry: {info.filename}")
        if info.file_size > MAX_ENTRY_BYTES:
            raise ValueError(f"Archive entry is too large: {info.filename}")
        total += info.file_size
        if total > MAX_TOTAL_BYTES:
            raise ValueError("Archive is too large.")
        unix_mode = info.external_attr >> 16
        if unix_mode and (unix_mode & 0o170000) == 0o120000:
            raise ValueError(f"Symbolic links are not allowed: {info.filename}")
    return entries


def unique_import_dir(global_root: Path) -> Path:
    stem = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    candidate = global_root / "imports" / stem
    suffix = 1
    while candidate.exists():
        candidate = global_root / "imports" / f"{stem}-{suffix}"
        suffix += 1
    return candidate


def import_profile(global_root: Path, bundle: Path) -> int:
    if not bundle.is_file():
        print(f"Bundle not found: {bundle}", file=sys.stderr)
        return 1
    try:
        with zipfile.ZipFile(bundle) as archive:
            entries = safe_entries(archive)
            manifest_name = f"{ROOT_NAME}/manifest.json"
            if manifest_name not in {entry.filename for entry in entries}:
                raise ValueError("Profile manifest is missing.")
            manifest = json.loads(archive.read(manifest_name).decode("utf-8"))
            if manifest.get("format") != 1:
                raise ValueError("Unsupported profile bundle format.")

            destination = unique_import_dir(global_root)
            destination.mkdir(parents=True, exist_ok=False)
            for name in PROFILE_FILES:
                archive_name = f"{ROOT_NAME}/{name}"
                if archive_name in {entry.filename for entry in entries}:
                    (destination / name).write_bytes(archive.read(archive_name))
            (destination / "manifest.json").write_text(
                json.dumps(manifest, indent=2), encoding="utf-8"
            )
    except (OSError, ValueError, KeyError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(f"Import failed: {exc}", file=sys.stderr)
        return 1

    print(destination)
    print("Import staged only. Run /profile to compare and merge; live files were not overwritten.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--global-dir", help="Override the global profile directory.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    export_parser = subparsers.add_parser("export", help="Export generalized global state.")
    export_parser.add_argument("--output", required=True, help="Output ZIP path.")

    import_parser = subparsers.add_parser(
        "import", help="Stage an imported profile for explicit merge."
    )
    import_parser.add_argument("--bundle", required=True, help="Profile ZIP path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    global_root = resolve_global_dir(args.global_dir)
    if args.command == "export":
        return export_profile(global_root, Path(args.output).expanduser().resolve())
    return import_profile(global_root, Path(args.bundle).expanduser().resolve())


if __name__ == "__main__":
    raise SystemExit(main())
