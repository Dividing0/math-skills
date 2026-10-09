"""Release archives retain Claude metadata while excluding repository artifacts."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from scripts.release_skills import package, validate_claude_metadata


class ReleaseMetadata(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.plugin = {
            "name": "math-skills",
            "version": "0.2.0",
            "description": "Mathematical skills",
            "author": {"name": "Test Maintainer"},
            "skills": ["./"],
        }
        self.marketplace = {
            "name": "math-skills",
            "owner": {"name": "Test Maintainer"},
            "plugins": [{"name": "math-skills", "source": "./"}],
        }
        self.write(".claude-plugin/plugin.json", json.dumps(self.plugin))
        self.write(".claude-plugin/marketplace.json", json.dumps(self.marketplace))
        self.write(
            "pyproject.toml", '[project]\nname = "math-skills"\nversion = "0.2.0"\n'
        )
        self.write(
            "sample-skill/SKILL.md",
            '---\nname: sample-skill\ndescription: "A sample skill."\n---\n\n'
            "# Sample\n\nRead [the reference](references/example.md).\n",
        )
        self.write(
            "sample-skill/agents/openai.yaml",
            'interface:\n  display_name: "Sample Skill"\n'
            '  short_description: "A skill for checking release metadata"\n'
            '  default_prompt: "Use $sample-skill for this task."\n',
        )
        self.write("sample-skill/references/example.md", "Sample reference.\n")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.track()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    def track(self):
        subprocess.run(["git", "add", "--all"], cwd=self.root, check=True)

    def test_archive_includes_metadata_and_excludes_service_files(self):
        excluded = [
            "tests/test_example.py",
            "scripts/tool.py",
            ".claude-plugin/private.json",
            ".venv/example.py",
            "sample-skill/.DS_Store",
            "sample-skill/__pycache__/example.pyc",
            "sample-skill/venv/example.py",
        ]
        for name in excluded:
            self.write(name, "not a release resource\n")
        self.track()
        output = self.root / "release.zip"
        package(self.root, output)
        with ZipFile(output) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(
                set(archive.namelist()),
                {
                    ".claude-plugin/plugin.json",
                    ".claude-plugin/marketplace.json",
                    "sample-skill/SKILL.md",
                    "sample-skill/agents/openai.yaml",
                    "sample-skill/references/example.md",
                },
            )
            self.assertEqual(
                json.loads(archive.read(".claude-plugin/plugin.json")), self.plugin
            )

    def test_rejects_version_drift_and_wrong_skill_location(self):
        for field, value in (("version", "0.1.0"), ("skills", ["./missing/"])):
            with self.subTest(field=field):
                self.write(
                    ".claude-plugin/plugin.json",
                    json.dumps(dict(self.plugin, **{field: value})),
                )
                with self.assertRaises(ValueError):
                    validate_claude_metadata(self.root)

    def test_rejects_catalog_pointing_outside_plugin(self):
        self.marketplace["plugins"] = [{"name": "math-skills", "source": "../other"}]
        self.write(".claude-plugin/marketplace.json", json.dumps(self.marketplace))
        with self.assertRaisesRegex(ValueError, "root plugin"):
            validate_claude_metadata(self.root)

    def test_rejects_untracked_metadata(self):
        subprocess.run(
            ["git", "rm", "--cached", "-q", ".claude-plugin/plugin.json"],
            cwd=self.root,
            check=True,
        )
        with self.assertRaisesRegex(ValueError, "must be tracked"):
            package(self.root, self.root / "release.zip")


if __name__ == "__main__":
    unittest.main()
