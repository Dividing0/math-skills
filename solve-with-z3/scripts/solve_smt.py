#!/usr/bin/env python3
"""Solve SMT-LIB assertions and retain sat, unsat and unknown outcomes."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("z3-solver",)
EVIDENCE = "solver-result-for-encoded-formula; not an independently checked proof"
EXAMPLE = {
    "smt2": "(declare-const x Int) (assert (> x 3)) (assert (< x 6))",
    "timeout_ms": 5000,
}


def compute(data):
    import z3

    source = data["smt2"]
    timeout = data.get("timeout_ms", 5000)
    if not isinstance(source, str) or not source.strip() or len(source) > 100000:
        raise ValueError("smt2 must be nonempty text of at most 100000 characters")
    if type(timeout) is not int or not 1 <= timeout <= 60000:
        raise ValueError("timeout_ms must be an integer in 1..60000")
    try:
        assertions = z3.parse_smt2_string(source)
        solver = z3.Solver()
        solver.set(timeout=timeout)
        # SMT-LIB can explicitly name symbols that match Z3's fresh-name format.
        # Keep tracking literals disjoint from all declarations in the assertions.
        symbols, seen = set(), set()
        pending = list(assertions)
        while pending:
            expression = pending.pop()
            if expression.get_id() in seen:
                continue
            seen.add(expression.get_id())
            if z3.is_app(expression):
                symbols.add(str(expression.decl().name()))
                pending.extend(expression.children())
            elif z3.is_quantifier(expression):
                pending.append(expression.body())
        labels = {}
        for index, assertion in enumerate(assertions):
            label = z3.FreshBool("skill_assertion")
            while str(label.decl().name()) in symbols:
                label = z3.FreshBool("skill_assertion")
            symbols.add(str(label.decl().name()))
            labels[str(label)] = index
            solver.assert_and_track(assertion, label)
        outcome = solver.check()
        result = {
            "solver_status": str(outcome),
            "assertions": len(assertions),
            "timeout_ms": timeout,
        }
        if outcome == z3.sat:
            model = solver.model()
            result["model"] = model.sexpr()
            result["assertion_evaluations"] = [
                str(model.eval(a, model_completion=True)) for a in assertions
            ]
        elif outcome == z3.unsat:
            result["core_assertion_indices"] = sorted(
                labels[str(label)] for label in solver.unsat_core()
            )
            result["core_is_minimal"] = False
        else:
            result["reason_unknown"] = solver.reason_unknown()
        return result
    except z3.Z3Exception as exc:
        raise ValueError(f"Z3 rejected the input: {exc}") from exc


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
