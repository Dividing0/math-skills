#!/usr/bin/env python3
"""Run pinned Lean positive and negative test files with explicit diagnostics."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import re
import subprocess
import sys
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "actual-Lean-checker-results; finite regression coverage only"
EXAMPLE = {
    "project": ".",
    "cases": [
        {"file": "Tests/Positive.lean", "expect": "success"},
        {"file": "Tests/Negative.lean", "expect": "error", "contains": "mismatch"},
    ],
    "timeout": 60,
}


def compute(data):
    root = Path(data["project"]).resolve()
    timeout = data.get("timeout", 60)
    cases = data["cases"]
    if not (root / "lean-toolchain").is_file():
        raise ValueError("project must contain lean-toolchain")
    if type(timeout) is not int or not 1 <= timeout <= 300:
        raise ValueError("timeout must be 1..300 seconds per command")
    if not isinstance(cases, list) or not 1 <= len(cases) <= 100:
        raise ValueError("supply 1..100 test cases")

    def run(command):
        try:
            p = subprocess.run(
                command,
                cwd=root,
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                timeout=timeout,
                check=False,
            )
            return {
                "command": command,
                "returncode": p.returncode,
                "stdout": p.stdout,
                "stderr": p.stderr,
                "timed_out": False,
            }
        except subprocess.TimeoutExpired as exc:

            def decoded(value):
                return (
                    value.decode(errors="replace")
                    if isinstance(value, bytes)
                    else (value or "")
                )

            return {
                "command": command,
                "returncode": None,
                "stdout": decoded(exc.stdout),
                "stderr": decoded(exc.stderr),
                "timed_out": True,
            }

    preflight = run(["lake", "env", "lean", "--version"])
    if preflight["returncode"] != 0:
        return {
            "passed": False,
            "preflight": preflight,
            "cases": [],
            "scope": "toolchain unavailable; no test result established",
        }
    results = []
    for case in cases:
        path = (root / case["file"]).resolve()
        if (
            not path.is_relative_to(root)
            or path.suffix != ".lean"
            or not path.is_file()
        ):
            raise ValueError(
                "test files must exist inside the project and end in .lean"
            )
        expected = case["expect"]
        needle = case.get("contains", "")
        if (
            expected not in {"success", "error"}
            or not isinstance(needle, str)
            or (expected == "error" and not needle.strip())
        ):
            raise ValueError(
                "expect must be success or error; negative cases require a diagnostic substring"
            )
        check = run(["lake", "env", "lean", str(path)])
        output = check["stdout"] + check["stderr"]
        code = check["returncode"]
        passed = not check["timed_out"] and needle in output
        if expected == "success":
            passed = (
                passed
                and code == 0
                and re.search(r"declaration uses .sorry.", output) is None
            )
        else:
            passed = passed and code is not None and code > 0
        results.append(dict(check, file=case["file"], expected=expected, passed=passed))
    return {
        "passed": all(check["passed"] for check in results),
        "preflight": preflight,
        "cases": results,
        "scope": "direct file checks; build imported targets first; explicit expected errors are not proof completion",
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
