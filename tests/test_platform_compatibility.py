"""Exercise native filesystem and process boundaries, including legacy locales."""

import hashlib
import importlib.util
import json
import locale
import os
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

from test_host_helpers import ROOT, load

HELPERS = sorted(ROOT.glob("*/scripts/*.py"))
LEGACY_LAUNCHER = (
    "import locale,runpy,sys; locale.setlocale(locale.LC_CTYPE,'C'); "
    "sys.argv=sys.argv[1:]; runpy.run_path(sys.argv[0],run_name='__main__')"
)


def invoke(path, *arguments, cwd=None, legacy=False):
    command = [sys.executable, "-B"]
    if legacy:
        command += ["-X", "utf8=0", "-c", LEGACY_LAUNCHER]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run(
        [*command, str(path), *map(str, arguments)],
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=90,
        check=False,
    )


def missing_dependency(completed):
    if completed.returncode == 0:
        return None
    for source in (completed.stdout.strip(), completed.stderr.strip()):
        if source.startswith("dependency_unavailable:"):
            return source
        try:
            payload = json.loads(source)
        except ValueError:
            continue
        if isinstance(payload, dict) and (
            payload.get("status") in {"dependency_missing", "dependency-unavailable"}
            or payload.get("error_type") == "ModuleNotFoundError"
        ):
            return source
    return None


class HelperFiles(unittest.TestCase):
    def test_all_script_command_lines(self):
        for path in [*HELPERS, ROOT / "scripts/release_skills.py"]:
            with self.subTest(helper=str(path.relative_to(ROOT))):
                completed = invoke(path, "--help")
                missing = missing_dependency(completed)
                if missing:
                    self.skipTest(missing)
                self.assertEqual(
                    completed.returncode, 0, completed.stdout + completed.stderr
                )
                self.assertIn("usage:", completed.stdout)

    def test_all_json_helpers_read_utf8_and_bom_files_in_legacy_locale(self):
        with tempfile.TemporaryDirectory(prefix="math paths ") as directory:
            root = Path(directory) / "проєкт з пробілом & дані"
            root.mkdir()
            (root / "lean-toolchain").write_text("test pin\n", encoding="utf-8")
            (root / "Main.lean").write_text("-- Є ∀\n", encoding="utf-8")
            for path in HELPERS:
                if '"--input"' not in path.read_text(encoding="utf-8"):
                    continue
                example = invoke(path, "--example")
                self.assertEqual(example.returncode, 0, example.stderr)
                data = json.loads(example.stdout)
                data["portability_note"] = "Є Ё ∀ — UTF-8"
                if "project" in data:
                    data["project"] = str(root)
                # Checker execution is tested separately with real subprocesses;
                # this input must reach validation without invoking an absent Lake.
                if path.parent.parent.name == "audit-lean4-proofs":
                    data["files"] = []
                elif path.parent.parent.name == "test-lean4-code":
                    data["cases"] = []
                source = json.dumps(data, ensure_ascii=False, indent=2)
                for encoding in ("utf-8", "utf-8-sig"):
                    with self.subTest(
                        helper=str(path.relative_to(ROOT)), encoding=encoding
                    ):
                        request = root / "запит з пробілом.json"
                        request.write_bytes(source.encode(encoding))
                        completed = invoke(
                            path, "--input", request, cwd=root, legacy=True
                        )
                        payload = json.loads(completed.stdout)
                        if path.parent.parent.name in {
                            "audit-lean4-proofs",
                            "test-lean4-code",
                        }:
                            self.assertEqual(completed.returncode, 1, completed.stderr)
                            self.assertEqual(payload["error_type"], "ValueError")
                        else:
                            self.assertEqual(
                                completed.returncode,
                                0,
                                completed.stdout + completed.stderr,
                            )
                            self.assertEqual(payload["status"], "completed")
                            self.assertEqual(
                                payload["input_sha256"],
                                hashlib.sha256(source.encode("utf-8")).hexdigest(),
                            )

    def test_utf8_lean_search_and_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "lean-toolchain").write_text("test pin\n", encoding="utf-8")
            (root / "Main.lean").write_text("-- Є ∀\n", encoding="utf-8")
            request = root / "search.json"
            request.write_text(
                json.dumps({"project": str(root), "query": "Є"}), encoding="utf-8"
            )
            searched = invoke(
                ROOT / "search-mathlib/scripts/search_local.py",
                "--input",
                request,
                legacy=True,
            )
            self.assertEqual(searched.returncode, 0, searched.stdout + searched.stderr)
            self.assertEqual(
                json.loads(searched.stdout)["result"]["matches"][0]["text"], "-- Є ∀"
            )
            request.write_text(json.dumps({"project": str(root)}), encoding="utf-8")
            snapshot = invoke(
                ROOT / "migrate-lean4-projects/scripts/project_snapshot.py",
                "--input",
                request,
                legacy=True,
            )
            self.assertEqual(snapshot.returncode, 0, snapshot.stdout + snapshot.stderr)
            self.assertEqual(
                json.loads(snapshot.stdout)["result"]["sources"]["Main.lean"],
                hashlib.sha256((root / "Main.lean").read_bytes()).hexdigest(),
            )

    def test_examples_use_the_working_directory_for_output(self):
        path = ROOT / "visualize-math-results/scripts/plot_data.py"
        example = json.loads(invoke(path, "--example").stdout)
        self.assertFalse(Path(example["output"]).is_absolute())
        with tempfile.TemporaryDirectory() as directory:
            request = Path(directory) / "plot.json"
            request.write_text(json.dumps(example), encoding="utf-8")
            completed = invoke(path, "--input", request, cwd=directory)
            self.assertEqual(
                completed.returncode, 0, completed.stdout + completed.stderr
            )
            output = Path(json.loads(completed.stdout)["result"]["output"])
            self.assertTrue(output.is_relative_to(Path(directory).resolve()))
            self.assertTrue(output.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))

    def test_all_available_example_self_tests(self):
        for path in HELPERS:
            if path.name != "example.py":
                continue
            with self.subTest(helper=str(path.relative_to(ROOT))):
                completed = invoke(path, "--self-test")
                missing = missing_dependency(completed)
                if missing:
                    self.skipTest(missing)
                self.assertEqual(
                    completed.returncode, 0, completed.stdout + completed.stderr
                )
                self.assertIsInstance(json.loads(completed.stdout), dict)


class NativeProcesses(unittest.TestCase):
    def test_runner_preserves_unicode_arguments_source_and_logs(self):
        tool = load("run-math-python", "run_math.py")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "робота з пробілом & (test)"
            root.mkdir()
            script = root / "завдання.py"
            script.write_text(
                "import json,os,sys\n"
                "sys.stdout.buffer.write(json.dumps({'args':sys.argv[1:], 'cwd':os.getcwd(),"
                "'value':'Є ∀'},ensure_ascii=False).encode('utf-8'))\n"
                "sys.stderr.buffer.write('Діагностика'.encode('utf-8'))\n",
                encoding="utf-8",
            )
            out = root / "результати з пробілом"
            arguments = ["space argument", 'literal"quote', "literal&value", "Є ∀"]
            result = tool.run(script, out, sys.executable, 20, arguments=arguments)
            self.assertEqual(result["status"], "completed")
            log = json.loads((out / "stdout.txt").read_text(encoding="utf-8"))
            self.assertEqual(log["args"], arguments)
            self.assertEqual(Path(log["cwd"]), out.resolve())
            self.assertEqual(log["value"], "Є ∀")
            self.assertEqual(
                (out / "stderr.txt").read_text(encoding="utf-8"), "Діагностика"
            )
            self.assertEqual((out / "source.py").read_bytes(), script.read_bytes())
            self.assertEqual(
                json.loads((out / "run.json").read_text(encoding="utf-8")), result
            )
            # Rename immediately to catch leaked file handles on Windows.
            out.rename(root / "closed logs")

    def test_runner_failure_timeout_and_temporary_cleanup(self):
        tool = load("run-math-python", "run_math.py")
        result = tool.self_test(sys.executable)
        self.assertEqual(result["status"], "pass")

    def test_checker_utf8_diagnostics_and_closed_temporary_file(self):
        audit = load("audit-lean4-proofs", "check_project.py")
        cases = load("test-lean4-code", "run_cases.py")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "Lean з пробілом"
            root.mkdir()
            (root / "lean-toolchain").write_text("test pin\n", encoding="utf-8")
            (root / "Main.lean").write_text("-- Є ∀\n", encoding="utf-8")
            checker = root / "checker.py"
            checker.write_text(
                "import pathlib,sys\n"
                "if sys.argv[-1]!='--version':\n"
                " p=pathlib.Path(sys.argv[-1]); text=p.read_text(encoding='utf-8')\n"
                " if p.name.startswith('SkillAudit'): assert '#print axioms Main.clean' in text\n"
                "sys.stdout.buffer.write('Є ∀: checked'.encode('utf-8'))\n"
                "sys.stderr.buffer.write('λ diagnostic'.encode('utf-8'))\n",
                encoding="utf-8",
            )
            real_run = subprocess.run

            def routed(command, **kwargs):
                self.assertEqual(command[:3], ["lake", "env", "lean"])
                return real_run([sys.executable, str(checker), *command[3:]], **kwargs)

            # Replace only the external checker executable; use native processes,
            # file opens and cleanup. This is not a Lean correctness test.
            previous = locale.setlocale(locale.LC_CTYPE)
            try:
                locale.setlocale(locale.LC_CTYPE, "C")
                with patch.object(audit.subprocess, "run", side_effect=routed):
                    result = audit.compute(
                        {
                            "project": str(root),
                            "modules": ["Main"],
                            "theorems": ["Main.clean"],
                        }
                    )
                    checked = cases.compute(
                        {
                            "project": str(root),
                            "cases": [
                                {
                                    "file": "Main.lean",
                                    "expect": "success",
                                    "contains": "Є ∀",
                                }
                            ],
                        }
                    )
            finally:
                locale.setlocale(locale.LC_CTYPE, previous)
            self.assertTrue(result["checker_success"])
            self.assertEqual(result["checks"][0]["stdout"], "Є ∀: checked")
            self.assertEqual(result["checks"][0]["stderr"], "λ diagnostic")
            self.assertTrue(checked["passed"])
            self.assertEqual(list(root.glob("SkillAudit*")), [])
            root.rename(root.with_name("removed handles"))

    @unittest.skipUnless(
        importlib.util.find_spec("ipykernel"), "Notebook runtime unavailable"
    )
    def test_notebook_kernel_and_temporary_directory_cleanup(self):
        # A restricted host can forbid local sockets entirely. Do not label that
        # as a notebook failure; native CI runners must still execute the kernel.
        with tempfile.TemporaryDirectory() as directory:
            family = socket.AF_UNIX if os.name == "posix" else socket.AF_INET
            try:
                with socket.socket(family, socket.SOCK_STREAM) as probe:
                    probe.bind(
                        str(Path(directory) / "probe")
                        if os.name == "posix"
                        else ("127.0.0.1", 0)
                    )
            except PermissionError as exc:
                self.skipTest(f"Host forbids local kernel sockets: {exc}")
        tool = load("run-math-python", "notebook_example.py")
        original = tempfile.TemporaryDirectory
        original_manager = tool.KernelManager
        created = []
        managers = []

        def temporary(*args, **kwargs):
            kwargs["prefix"] = "math kernel Є "
            folder = original(*args, **kwargs)
            created.append(Path(folder.name))
            return folder

        def manager(*args, **kwargs):
            kernel = original_manager(*args, **kwargs)
            managers.append(kernel)
            return kernel

        with original() as directory:
            output = Path(directory) / "нотатник з пробілом.ipynb"
            with (
                patch.object(
                    tool.tempfile, "TemporaryDirectory", side_effect=temporary
                ),
                patch.object(tool, "KernelManager", side_effect=manager),
            ):
                result = tool.execute(str(output))
            self.assertEqual(result["value"], 42)
            self.assertEqual(
                Path(result["kernel_executable"]).resolve(),
                Path(sys.executable).resolve(),
            )
            cells = json.loads(output.read_text(encoding="utf-8"))["cells"]
            self.assertTrue(all(cell["execution_count"] for cell in cells))
        self.assertTrue(created)
        self.assertTrue(all(not path.exists() for path in created))
        self.assertTrue(managers)
        self.assertTrue(all(not kernel.has_kernel for kernel in managers))


class ReleaseProcess(unittest.TestCase):
    def test_release_cli_from_other_directory_and_extracted_helper(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "пакування з пробілом & дані"
            output = root / "nested" / "скілі.zip"
            root.mkdir()
            completed = invoke(
                ROOT / "scripts/release_skills.py",
                "--output",
                output,
                cwd=root,
                legacy=True,
            )
            self.assertEqual(
                completed.returncode, 0, completed.stdout + completed.stderr
            )
            extracted = root / "extracted"
            with ZipFile(output) as archive:
                self.assertIsNone(archive.testzip())
                self.assertTrue(
                    all(
                        "\\" not in name and not name.startswith("/")
                        for name in archive.namelist()
                    )
                )
                archive.extractall(extracted)
            request = root / "запит.json"
            request.write_text('{"operation":"bezout","a":12,"b":18}', encoding="utf-8")
            helper = extracted / "research-number-theory/scripts/integer_tools.py"
            result = invoke(helper, "--input", request, cwd=root)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(json.loads(result.stdout)["result"]["gcd"], 6)


if __name__ == "__main__":
    unittest.main()
