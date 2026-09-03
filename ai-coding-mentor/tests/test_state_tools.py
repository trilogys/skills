from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INIT = ROOT / "scripts" / "init_state.py"
COLLECT = ROOT / "scripts" / "collect_monthly_context.py"
PORTABLE = ROOT / "scripts" / "profile_portability.py"


def run_script(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args],
        text=True,
        capture_output=True,
        check=False,
    )


class StateToolTests(unittest.TestCase):
    def test_init_all_creates_both_scopes_without_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            project = root / "project"
            global_dir = root / "global"
            project.mkdir()

            first = run_script(
                INIT,
                "--scope",
                "all",
                "--project-dir",
                str(project),
                "--global-dir",
                str(global_dir),
                "--mentor-level",
                "2",
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertTrue((global_dir / "GLOBAL_PROFILE.md").is_file())
            self.assertTrue((project / ".ai-mentor" / "PROJECT_PROFILE.md").is_file())
            self.assertIn(
                "Default mentor level: `L2`",
                (project / ".ai-mentor" / "MENTOR_CONFIG.md").read_text(),
            )

            profile = global_dir / "GLOBAL_PROFILE.md"
            profile.write_text("keep-me", encoding="utf-8")
            second = run_script(
                INIT,
                "--scope",
                "all",
                "--project-dir",
                str(project),
                "--global-dir",
                str(global_dir),
                "--mentor-level",
                "4",
            )
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(profile.read_text(encoding="utf-8"), "keep-me")

    def test_init_preserves_legacy_v2_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp) / "project"
            mentor = project / ".ai-mentor"
            mentor.mkdir(parents=True)
            legacy = mentor / "CAPABILITY_PROFILE.md"
            legacy.write_text("legacy-evidence", encoding="utf-8")

            result = run_script(
                INIT, "--scope", "project", "--project-dir", str(project)
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(legacy.read_text(encoding="utf-8"), "legacy-evidence")
            self.assertIn("Legacy V2 state detected", result.stdout)

    def test_monthly_collector_includes_project_and_global_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            project = root / "project"
            global_dir = root / "global"
            project.mkdir()
            init = run_script(
                INIT,
                "--scope",
                "all",
                "--project-dir",
                str(project),
                "--global-dir",
                str(global_dir),
            )
            self.assertEqual(init.returncode, 0, init.stderr)

            (project / ".ai-mentor" / "PROJECT_EVIDENCE.md").write_text(
                "2026-09 user found a transaction defect", encoding="utf-8"
            )
            (global_dir / "EVIDENCE_LEDGER.md").write_text(
                "generalized review evidence", encoding="utf-8"
            )
            result = run_script(
                COLLECT,
                "--month",
                "2026-09",
                "--project-dir",
                str(project),
                "--global-dir",
                str(global_dir),
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            output = project / ".ai-mentor" / "reports" / "2026-09-evidence.md"
            text = output.read_text(encoding="utf-8")
            self.assertIn("transaction defect", text)
            self.assertIn("generalized review evidence", text)
            self.assertIn("does not assign or promote", text)

            invalid = run_script(
                COLLECT,
                "--month",
                "2026-13",
                "--project-dir",
                str(project),
            )
            self.assertEqual(invalid.returncode, 2)

    def test_profile_export_and_staged_import_do_not_overwrite_live_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source-profile"
            target = root / "target-profile"
            bundle = root / "profile.zip"
            project = root / "project"
            project.mkdir()
            init = run_script(
                INIT,
                "--scope",
                "global",
                "--project-dir",
                str(project),
                "--global-dir",
                str(source),
            )
            self.assertEqual(init.returncode, 0, init.stderr)
            (source / "GLOBAL_PROFILE.md").write_text(
                "portable-evidence", encoding="utf-8"
            )

            exported = run_script(
                PORTABLE,
                "--global-dir",
                str(source),
                "export",
                "--output",
                str(bundle),
            )
            self.assertEqual(exported.returncode, 0, exported.stderr)
            (target / "imports").mkdir(parents=True)
            live = target / "GLOBAL_PROFILE.md"
            live.write_text("live-profile", encoding="utf-8")

            imported = run_script(
                PORTABLE,
                "--global-dir",
                str(target),
                "import",
                "--bundle",
                str(bundle),
            )
            self.assertEqual(imported.returncode, 0, imported.stderr)
            self.assertEqual(live.read_text(encoding="utf-8"), "live-profile")
            staged = list((target / "imports").glob("*/GLOBAL_PROFILE.md"))
            self.assertEqual(len(staged), 1)
            self.assertEqual(staged[0].read_text(encoding="utf-8"), "portable-evidence")

    def test_profile_import_rejects_path_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            bundle = root / "malicious.zip"
            target = root / "target"
            with zipfile.ZipFile(bundle, "w") as archive:
                archive.writestr("../../outside.txt", "bad")

            result = run_script(
                PORTABLE,
                "--global-dir",
                str(target),
                "import",
                "--bundle",
                str(bundle),
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((root / "outside.txt").exists())


if __name__ == "__main__":
    unittest.main()
