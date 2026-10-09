#!/usr/bin/env python3
"""Exhaustively check a classical propositional formula encoded as a JSON tree."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from itertools import product
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-computation"
EXAMPLE = {"formula": ["implies", ["and", ["implies", "P", "Q"], "P"], "Q"]}


def compute(data):
    names = set()

    def inspect(node):
        if type(node) is bool:
            return
        if isinstance(node, str):
            names.add(node)
            return
        if not isinstance(node, list) or not node:
            raise ValueError(
                "formula must be a Boolean, variable string, or [operator, ...]"
            )
        op = node[0]
        arity = {"not": 1, "and": 2, "or": 2, "implies": 2, "iff": 2}.get(op)
        if arity is None or len(node) != arity + 1:
            raise ValueError("invalid operator or arity")
        for child in node[1:]:
            inspect(child)

    formula = data["formula"]
    inspect(formula)
    if len(names) > 16:
        raise ValueError("at most 16 variables are supported")
    variables = sorted(names)

    def evaluate(node, assignment):
        if type(node) is bool:
            return node
        if isinstance(node, str):
            return assignment[node]
        op, *children = node
        values = [evaluate(child, assignment) for child in children]
        if op == "not":
            return not values[0]
        a, b = values
        return {"and": a and b, "or": a or b, "implies": not a or b, "iff": a == b}[op]

    count, model, countermodel = 0, None, None
    for values in product((False, True), repeat=len(variables)):
        assignment = dict(zip(variables, values))
        if evaluate(formula, assignment):
            count += 1
            if model is None:
                model = assignment
        elif countermodel is None:
            countermodel = assignment
    return {
        "variables": variables,
        "valuations_checked": 2 ** len(variables),
        "satisfying_valuations": count,
        "valid": count == 2 ** len(variables),
        "satisfiable": count > 0,
        "model": model,
        "countermodel": countermodel,
        "logic": "classical propositional; no first-order or proof-system claim",
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
