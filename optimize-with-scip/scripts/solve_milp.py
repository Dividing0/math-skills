#!/usr/bin/env python3
"""Solve a bounded-size linear mixed-integer model with SCIP diagnostics."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("pyscipopt",)
EVIDENCE = "floating-point-MILP-solver-evidence; not an exact certificate"
EXAMPLE = {
    "variables": [
        {"name": "x", "type": "I", "lower": 0, "upper": 10},
        {"name": "y", "type": "B"},
    ],
    "objective": [3, 2],
    "sense": "maximize",
    "constraints": [{"coefficients": [2, 1], "sense": "<=", "rhs": 4}],
    "time_limit": 5,
}


def number(value):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError("numeric inputs must be finite JSON numbers")
    return float(value)


def compute(data):
    from pyscipopt import Model, quicksum

    specs = data["variables"]
    constraints = data.get("constraints", [])
    if (
        not isinstance(specs, list)
        or not 1 <= len(specs) <= 200
        or len(constraints) > 2000
    ):
        raise ValueError("use 1..200 variables and at most 2000 constraints")
    names = [v["name"] for v in specs]
    if any(
        not isinstance(name, str) or not name.isidentifier() for name in names
    ) or len(set(names)) != len(names):
        raise ValueError("variable names must be distinct identifiers")
    limit = number(data.get("time_limit", 10))
    if not 0 < limit <= 300:
        raise ValueError("time_limit must be in (0,300] seconds")
    sense = data.get("sense", "minimize")
    if sense not in {"minimize", "maximize"}:
        raise ValueError("sense must be minimize or maximize")
    model = Model("skill_model")
    model.hideOutput()
    model.setRealParam("limits/time", limit)
    variables, bounds = [], []
    for spec in specs:
        kind = spec.get("type", "C")
        if kind not in {"C", "I", "B"}:
            raise ValueError("variable type must be C, I or B")
        lower = None if spec.get("lower", 0) is None else number(spec.get("lower", 0))
        upper = None if spec.get("upper") is None else number(spec["upper"])
        if kind == "B":
            lower = max(0.0, lower if lower is not None else 0.0)
            upper = min(1.0, upper if upper is not None else 1.0)
        if lower is not None and upper is not None and lower > upper:
            raise ValueError("variable lower bound exceeds upper bound")
        bounds.append((lower, upper, kind))
        variables.append(
            model.addVar(name=spec["name"], vtype=kind, lb=lower, ub=upper)
        )

    def coefficients(values):
        if len(values) != len(variables):
            raise ValueError("coefficient count must match variables")
        return list(map(number, values))

    objective = coefficients(data["objective"])
    model.setObjective(quicksum(c * v for c, v in zip(objective, variables)), sense)
    rows = []
    for row in constraints:
        coeff = coefficients(row["coefficients"])
        rhs = number(row["rhs"])
        relation = row["sense"]
        lhs = quicksum(c * v for c, v in zip(coeff, variables))
        if relation == "<=":
            model.addCons(lhs <= rhs)
        elif relation == ">=":
            model.addCons(lhs >= rhs)
        elif relation == "==":
            model.addCons(lhs == rhs)
        else:
            raise ValueError("constraint sense must be <=, >= or ==")
        rows.append((coeff, relation, rhs))
    model.optimize()

    def finite_bound(value):
        return (
            float(value)
            if math.isfinite(value) and abs(value) < model.infinity()
            else None
        )

    result = {
        "solver_status": str(model.getStatus()),
        "solution_count": model.getNSols(),
        "sense": sense,
        "dual_bound": finite_bound(model.getDualbound()),
        "primal_bound": finite_bound(model.getPrimalbound()),
    }
    if model.getNSols() > 0:
        solution = model.getBestSol()
        x = [float(model.getSolVal(solution, v)) for v in variables]
        violations = [0.0]
        for value, (lower, upper, kind) in zip(x, bounds):
            violations.extend(
                [
                    max(0, lower - value) if lower is not None else 0,
                    max(0, value - upper) if upper is not None else 0,
                ]
            )
        for coeff, relation, rhs in rows:
            residual = sum(c * v for c, v in zip(coeff, x)) - rhs
            violations.append(
                abs(residual)
                if relation == "=="
                else max(0, residual if relation == "<=" else -residual)
            )
        result.update(
            solution=dict(zip(names, x)),
            objective=sum(c * v for c, v in zip(objective, x)),
            max_feasibility_violation=max(violations),
            max_integrality_residual=max(
                [0.0]
                + [
                    abs(v - round(v))
                    for v, (_, _, kind) in zip(x, bounds)
                    if kind != "C"
                ]
            ),
            relative_gap=finite_bound(model.getGap())
            if result["primal_bound"] is not None and result["dual_bound"] is not None
            else None,
        )
    return result


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
