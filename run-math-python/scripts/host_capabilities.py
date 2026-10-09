#!/usr/bin/env python3
"""Report host interpreters, executables and installed package metadata without installing dependencies."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import shutil
import sys
import sysconfig
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "host-environment-inventory"
EXAMPLE = {}


def compute(data):
    packages = data.get(
        "packages",
        [
            "numpy",
            "scipy",
            "sympy",
            "networkx",
            "mpmath",
            "python-flint",
            "statsmodels",
            "matplotlib",
            "cvxpy",
            "jax",
            "pymc",
            "gudhi",
        ],
    )
    executables = data.get(
        "executables", ["python3", "uv", "lean", "lake", "sage", "jupyter", "pdflatex"]
    )
    if any(not isinstance(v, str) or not v for v in packages + executables):
        raise ValueError("package and executable names must be nonempty strings")
    versions = {}
    for package in packages:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    return {
        "interpreter": sys.executable,
        "platform": platform.platform(),
        "implementation": platform.python_implementation(),
        "site_packages": sysconfig.get_paths()["purelib"],
        "packages": versions,
        "executables": {name: shutil.which(name) for name in executables},
        "scope": "installed metadata and PATH discovery; imports, solvers and accelerators are not tested",
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
        source = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
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
