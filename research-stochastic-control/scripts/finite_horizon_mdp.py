#!/usr/bin/env python3
"""Solve a fully observed finite-horizon MDP by exact rational backward induction."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from fractions import Fraction
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-horizon-dynamic-programming"
EXAMPLE = {
    "transitions": [[[1, 0], [0, 1]], [[0, 1], [1, 0]]],
    "costs": [[1, 0], [0, 2]],
    "terminal_costs": [0, 3],
    "horizon": 2,
    "discount": "1",
}


def rational(value):
    if type(value) not in (int, str):
        raise TypeError("exact inputs must be integers or rational strings")
    return Fraction(value)


def compute(data):
    transitions, costs = data["transitions"], data["costs"]
    n, horizon = len(transitions), data["horizon"]
    if not 1 <= n <= 50 or type(horizon) is not int or not 0 <= horizon <= 100:
        raise ValueError("use 1..50 states and an integer horizon in 0..100")
    if len(costs) != n or any(not 1 <= len(actions) <= 20 for actions in transitions):
        raise ValueError("each state needs 1..20 actions and matching costs")
    P, c = [], []
    for actions, state_costs in zip(transitions, costs):
        if len(actions) != len(state_costs):
            raise ValueError("one cost per available action is required")
        parsed = [list(map(rational, row)) for row in actions]
        if any(len(row) != n or min(row) < 0 or sum(row) != 1 for row in parsed):
            raise ValueError(
                "transition rows must be exact probability vectors over states"
            )
        P.append(parsed)
        c.append(list(map(rational, state_costs)))
    terminal = list(map(rational, data.get("terminal_costs", [0] * n)))
    discount = rational(data.get("discount", 1))
    if len(terminal) != n or not 0 <= discount <= 1:
        raise ValueError(
            "terminal costs must match states and discount must be in [0,1]"
        )
    values, policies = [terminal], []
    for _ in range(horizon):
        next_value = values[0]
        candidates = [
            [
                cost
                + discount * sum((p * v for p, v in zip(row, next_value)), Fraction(0))
                for cost, row in zip(c[s], P[s])
            ]
            for s in range(n)
        ]
        policy = [min(range(len(q)), key=lambda a: q[a]) for q in candidates]
        values.insert(0, [q[a] for q, a in zip(candidates, policy)])
        policies.insert(0, policy)
    return {
        "values_by_time": [list(map(str, row)) for row in values],
        "policy_by_time": policies,
        "horizon": horizon,
        "discount": str(discount),
        "optimization": "minimum expected discounted cost",
        "tie_break": "lowest action index",
        "scope": "known finite fully observed Markov model; not partial observation, continuous control or infinite horizon",
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
