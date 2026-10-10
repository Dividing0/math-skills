#!/usr/bin/env python3
"""Run pinned Lean file checks and named theorem axiom diagnostics with captured host output."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import re
import subprocess
import sys
import tempfile
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "formal-checker-execution-not-statement-correspondence"
EXAMPLE = {"project": ".", "files": ["Main.lean"], "timeout": 60}


def compute(data):
    project = Path(data["project"]).resolve()
    timeout = float(data.get("timeout", 60))
    if (
        not project.is_dir()
        or not (project / "lean-toolchain").is_file()
        or not 0 < timeout <= 3600
    ):
        raise ValueError(
            "project must contain lean-toolchain and timeout must be in (0,3600]"
        )
    files = data.get("files", [])
    modules = data.get("modules", [])
    theorems = data.get("theorems", [])
    if not files and not theorems:
        raise ValueError("supply files or theorem names to check")
    identifier = r"[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*"
    if any(
        not isinstance(name, str) or not re.fullmatch(identifier, name)
        for name in modules + theorems
    ):
        raise ValueError(
            "module and theorem names must be simple dotted Lean identifiers"
        )
    records = []

    def run(command):
        try:
            process = subprocess.run(
                command,
                cwd=project,
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                timeout=timeout,
                check=False,
            )
            return {
                "command": command,
                "returncode": process.returncode,
                "stdout": process.stdout,
                "stderr": process.stderr,
                "timed_out": False,
            }
        except subprocess.TimeoutExpired as exc:
            return {
                "command": command,
                "returncode": None,
                "stdout": (exc.stdout or b"").decode(errors="replace")
                if isinstance(exc.stdout, bytes)
                else (exc.stdout or ""),
                "stderr": (exc.stderr or b"").decode(errors="replace")
                if isinstance(exc.stderr, bytes)
                else (exc.stderr or ""),
                "timed_out": True,
            }

    for filename in files:
        path = (project / filename).resolve()
        if (
            not path.is_relative_to(project)
            or not path.is_file()
            or path.suffix != ".lean"
        ):
            raise ValueError("files must be Lean sources inside the project")
        records.append(run(["lake", "env", "lean", str(path)]))
    if theorems:
        if not modules:
            raise ValueError(
                "theorem audits require modules to import; build those modules first"
            )
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            suffix=".lean",
            prefix="SkillAudit",
            dir=project,
            delete=False,
        ) as scratch:
            scratch.write("".join(f"import {name}\n" for name in modules))
            scratch.write(
                "".join(f"#check {name}\n#print axioms {name}\n" for name in theorems)
            )
            path = Path(scratch.name)
        try:
            records.append(run(["lake", "env", "lean", str(path)]))
        finally:
            path.unlink(missing_ok=True)
    text = "\n".join(record["stdout"] + "\n" + record["stderr"] for record in records)
    return {
        "toolchain": (project / "lean-toolchain").read_text(encoding="utf-8").strip(),
        "checks": records,
        "checker_success": all(record["returncode"] == 0 for record in records),
        "sorry_marker_detected": bool(
            re.search(r"\bsorryAx\b|declaration uses .sorry.", text)
        ),
        "scope": "actual checker output; statement correspondence and interpretation of axioms require review",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="-", help="JSON file, or - for stdin")
    parser.add_argument(
        "--example", action="store_true", help="Print an example input and exit"
    )
    args = parser.parse_args()
    if args.example:
        print(json.dumps(EXAMPLE, indent=2))
        return 0
    try:
        source = (
            sys.stdin.read()
            if args.input == "-"
            else Path(args.input).read_text(encoding="utf-8-sig")
        )
        data = json.loads(source, parse_constant=reject_constant)
        if not isinstance(data, dict):
            raise TypeError("input must be a JSON object")
        result = compute(data)
        payload = {
            "status": "completed",
            "evidence": EVIDENCE,
            "result": result,
            "input_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "versions": {
                "python": platform.python_version(),
                **{name: importlib.metadata.version(name) for name in DEPENDENCIES},
            },
        }
        print(json.dumps(payload, indent=2, allow_nan=False))
        return 0
    except ImportError as exc:
        print(json.dumps({"status": "dependency_missing", "error": str(exc)}))
        return 3
    except (
        ValueError,
        TypeError,
        KeyError,
        IndexError,
        ArithmeticError,
        OSError,
        SyntaxError,
        RuntimeError,
        NotImplementedError,
    ) as exc:
        print(
            json.dumps(
                {
                    "status": "failed",
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )
        )
        return 1


def reject_constant(value):
    raise ValueError(f"nonfinite JSON number: {value}")


if __name__ == "__main__":
    sys.exit(main())
