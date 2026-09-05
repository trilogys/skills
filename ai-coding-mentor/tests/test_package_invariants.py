from __future__ import annotations

import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"


class PackageInvariantTests(unittest.TestCase):
    def test_skill_name_matches_folder_and_core_stays_compact(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        match = re.search(r"^name:\s*([^\s]+)$", text, re.MULTILINE)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), ROOT.name)
        self.assertLessEqual(len(text.splitlines()), 500)

    def test_every_local_markdown_link_resolves(self) -> None:
        sources = [SKILL, *sorted((ROOT / "references").glob("*.md"))]
        local_links = 0
        for source in sources:
            text = source.read_text(encoding="utf-8")
            paths = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
            for relative in paths:
                if "://" in relative or relative.startswith("#"):
                    continue
                local_links += 1
                target = relative.split("#", 1)[0]
                self.assertTrue((source.parent / target).is_file(), f"{source}: {relative}")
        self.assertGreater(local_links, 0)

    def test_learning_export_resources_are_complete(self) -> None:
        expected = (
            "references/learning-export-guide.md",
            "templates/DAILY_LEARNING_REPORT.md",
            "templates/WEEKLY_LEARNING_REPORT.md",
            "templates/MONTHLY_REPORT.md",
        )
        for relative in expected:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_learning_exports_are_explicit_by_default(self) -> None:
        skill_text = SKILL.read_text(encoding="utf-8")
        global_settings = (ROOT / "templates" / "GLOBAL_SETTINGS.md").read_text(
            encoding="utf-8"
        )
        project_settings = (ROOT / "templates" / "MENTOR_CONFIG.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Do not auto-export after routine tasks", skill_text)
        self.assertIn("Automatic learning report exports: No", global_settings)
        self.assertIn("Automatic learning report exports: No", project_settings)

    def test_default_is_work_first_l1(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("use `/normal` with mentor level `L1`", text)
        self.assertIn("L1 | Work first", text)

    def test_scripts_expose_help(self) -> None:
        for script in sorted((ROOT / "scripts").glob("*.py")):
            result = subprocess.run(
                [sys.executable, str(script), "--help"],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, f"{script.name}: {result.stderr}")


if __name__ == "__main__":
    unittest.main()
