#!/usr/bin/env python3
"""Run exact symbolic algebra, calculus, matrix, dynamics and local metric calculations."""

import argparse
import ast
import hashlib
import importlib.metadata
import json
import operator
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("sympy",)
EVIDENCE = "symbolic-computation-with-domain-obligations"
EXAMPLE = {
    "operation": "solve",
    "symbols": {"x": {"real": True}},
    "expression": "(x**2 - 1)/(x - 1) - 2",
    "variable": "x",
}


def compute(data):
    import sympy as sp

    specifications = data.get("symbols", {"x": {"real": True}})
    if not isinstance(specifications, dict) or len(specifications) > 20:
        raise ValueError("symbols must map at most 20 names to assumptions")
    names = {}
    for name, assumptions in specifications.items():
        if (
            not isinstance(name, str)
            or not name.isidentifier()
            or name.startswith("_")
            or not isinstance(assumptions, dict)
        ):
            raise ValueError("invalid symbol declaration")
        if any(
            k not in {"real", "positive", "nonnegative", "nonzero", "integer"}
            or type(v) is not bool
            for k, v in assumptions.items()
        ):
            raise ValueError("unsupported symbol assumption")
        names[name] = sp.Symbol(name, **assumptions)
    functions = {
        name: getattr(sp, name)
        for name in ("sin", "cos", "tan", "exp", "log", "sqrt", "Abs", "sinh", "cosh")
    }
    if set(names) & (set(functions) | {"pi", "E", "I"}):
        raise ValueError("symbol name conflicts with a function or constant")
    constants = {"pi": sp.pi, "E": sp.E, "I": sp.I}
    denominators = []

    def expression(text):
        if type(text) is int:
            return sp.Integer(text)
        if not isinstance(text, str) or len(text) > 4096:
            raise ValueError(
                "expressions must be strings of at most 4096 characters, or integers"
            )
        tree = ast.parse(text, mode="eval")
        if sum(1 for _ in ast.walk(tree)) > 512:
            raise ValueError("expression tree is too large")

        def visit(node):
            if isinstance(node, ast.Constant) and type(node.value) in (int, float):
                return sp.Rational(ast.get_source_segment(text, node))
            if isinstance(node, ast.Name) and node.id in names | constants:
                return (names | constants)[node.id]
            if isinstance(node, ast.UnaryOp) and isinstance(
                node.op, (ast.UAdd, ast.USub)
            ):
                value = visit(node.operand)
                return -value if isinstance(node.op, ast.USub) else value
            if isinstance(node, ast.BinOp):
                a, b = visit(node.left), visit(node.right)
                if isinstance(node.op, ast.Div):
                    if b == 0:
                        raise ValueError("division by zero")
                    denominators.append(b)
                    return a / b
                if isinstance(node.op, ast.Pow):
                    if b.is_number and (b.is_real is not True or abs(b) > 1000):
                        raise ValueError(
                            "numeric exponents must be real and bounded by 1000"
                        )
                    if b.is_negative:
                        if a == 0:
                            raise ValueError("zero cannot have a negative power")
                        denominators.append(a)
                    return a**b
                function = {
                    ast.Add: operator.add,
                    ast.Sub: operator.sub,
                    ast.Mult: operator.mul,
                }.get(type(node.op))
                if function:
                    return function(a, b)
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id in functions
                and len(node.args) == 1
                and not node.keywords
            ):
                return functions[node.func.id](visit(node.args[0]))
            raise ValueError(
                "unsupported syntax; use declared symbols, arithmetic and listed unary functions"
            )

        return visit(tree.body)

    def matrix(values):
        if (
            not values
            or not values[0]
            or len(values) > 20
            or len(values[0]) > 20
            or any(len(row) != len(values[0]) for row in values)
        ):
            raise ValueError(
                "matrix must be rectangular, nonempty and at most 20 by 20"
            )
        return sp.Matrix([[expression(v) for v in row] for row in values])

    def encode(value):
        if isinstance(value, sp.MatrixBase):
            return [[str(v) for v in row] for row in value.tolist()]
        if isinstance(value, list):
            return [encode(v) for v in value]
        return str(value)

    operation = data["operation"]
    if operation in {
        "simplify",
        "factor",
        "expand",
        "differentiate",
        "integrate",
        "series",
        "solve",
        "residue",
    }:
        expr = expression(data["expression"])
        variable = (
            names[data.get("variable", "x")]
            if operation not in {"simplify", "factor", "expand"}
            else None
        )
        result = {"input_expression": str(expr)}
        if operation in {"simplify", "factor", "expand"}:
            result["value"] = str(getattr(sp, operation)(expr))
        elif operation == "differentiate":
            order = data.get("order", 1)
            if type(order) is not int or not 0 <= order <= 20:
                raise ValueError("derivative order must be 0..20")
            result["value"] = str(sp.diff(expr, variable, order))
        elif operation == "integrate":
            value = sp.integrate(expr, variable)
            result.update(
                value=str(value),
                derivative_residual=str(sp.simplify(sp.diff(value, variable) - expr)),
                unresolved_integral=bool(value.has(sp.Integral)),
            )
        elif operation == "series":
            order = data.get("order", 6)
            if type(order) is not int or not 1 <= order <= 30:
                raise ValueError("series order must be 1..30")
            result["value"] = str(
                sp.series(
                    expr,
                    variable,
                    expression(data.get("point", 0)),
                    order,
                    dir=data.get("direction", "+"),
                )
            )
        elif operation == "residue":
            result["value"] = str(
                sp.residue(expr, variable, expression(data.get("point", 0)))
            )
        else:
            domain_name = data.get("domain", "real")
            if domain_name not in {"real", "complex"}:
                raise ValueError("domain must be real or complex")
            domain = sp.S.Reals if domain_name == "real" else sp.S.Complexes
            assumption_sets = {
                "real": sp.S.Reals,
                "integer": sp.S.Integers,
                "positive": sp.Interval.open(0, sp.oo),
                "nonnegative": sp.Interval(0, sp.oo),
                "nonzero": sp.S.Reals - sp.FiniteSet(0),
            }
            for assumption, enabled in specifications[str(variable)].items():
                allowed = assumption_sets[assumption]
                domain = domain.intersect(allowed) if enabled else domain - allowed
            roots = sp.solveset(expr, variable, domain=domain)
            excluded = sp.S.EmptySet
            for denominator in denominators:
                excluded = sp.Union(
                    excluded, sp.solveset(denominator, variable, domain=domain)
                )
            solution = roots - excluded
            result.update(
                value=str(solution),
                effective_domain=str(domain),
                excluded=str(excluded),
                unresolved=bool(solution.has(sp.ConditionSet)),
            )
            if isinstance(solution, sp.FiniteSet):
                result["substitution_residuals"] = [
                    str(sp.simplify(expr.subs(variable, x))) for x in solution
                ]
    elif operation == "matrix":
        A = matrix(data["matrix"])
        rref, pivots = A.rref()
        basis = A.nullspace()
        result = {
            "shape": list(A.shape),
            "rank": A.rank(),
            "rref": encode(rref),
            "pivots": list(pivots),
            "nullspace": encode(basis),
            "nullspace_residuals": encode([A * v for v in basis]),
            "parameter_note": "symbolic rank may change at exceptional parameter values",
        }
        if A.rows == A.cols:
            result.update(
                determinant=str(A.det()),
                characteristic_polynomial=str(A.charpoly().as_expr()),
            )
        if "rhs" in data:
            b = sp.Matrix([expression(v) for v in data["rhs"]])
            if b.rows != A.rows:
                raise ValueError("rhs length does not match rows")
            result["solutions"] = str(sp.linsolve((A, b)))
    elif operation == "groebner":
        variables = [names[name] for name in data["variables"]]
        if not variables or len(set(variables)) != len(variables):
            raise ValueError("variables must be distinct and nonempty")
        polynomials = [expression(v) for v in data["polynomials"]]
        if not polynomials:
            raise ValueError("at least one generator is required")
        basis = sp.groebner(
            polynomials, *variables, domain=sp.QQ, order=data.get("order", "lex")
        )
        result = {
            "basis": [str(v) for v in basis],
            "domain": "QQ",
            "order": str(basis.order),
            "generator_remainders": [str(basis.reduce(v)[1]) for v in polynomials],
        }
        if "query" in data:
            query = expression(data["query"])
            quotient, remainder = basis.reduce(query)
            result.update(
                query_remainder=str(remainder),
                member=remainder == 0,
                reconstruction_residual=str(
                    sp.expand(
                        query - sum(q * g for q, g in zip(quotient, basis)) - remainder
                    )
                ),
            )
    elif operation == "dynamics":
        variables = [names[name] for name in data["variables"]]
        field = sp.Matrix([expression(v) for v in data["field"]])
        if (
            not variables
            or len(set(variables)) != len(variables)
            or field.rows != len(variables)
        ):
            raise ValueError("field must match distinct state variables")
        jacobian = field.jacobian(variables)
        result = {
            "jacobian": encode(jacobian),
            "scope": "autonomous field; symbolic identities are conditional on domains",
        }
        if "invariant" in data:
            invariant = expression(data["invariant"])
            derivative = sp.simplify(
                sum(sp.diff(invariant, x) * f for x, f in zip(variables, field))
            )
            result.update(
                lie_derivative=str(derivative), formal_invariant=derivative == 0
            )
        if "point" in data:
            if len(data["point"]) != len(variables):
                raise ValueError("point has wrong dimension")
            point = dict(zip(variables, map(expression, data["point"])))
            residual = field.subs(point, simultaneous=True).applyfunc(sp.simplify)
            result.update(
                point_residual=encode(residual),
                equilibrium_verified=all(v == 0 for v in residual),
                jacobian_at_point=encode(jacobian.subs(point, simultaneous=True)),
            )
    elif operation == "metric":
        coordinates = [names[name] for name in data["coordinates"]]
        n = len(coordinates)
        g = matrix(data["metric"])
        if (
            not 1 <= n <= 3
            or len(set(coordinates)) != n
            or g.shape != (n, n)
            or any(sp.simplify(v) != 0 for v in g - g.T)
        ):
            raise ValueError(
                "metric must be symmetric and match 1..3 distinct coordinates"
            )
        determinant = sp.simplify(g.det())
        if determinant == 0:
            raise ValueError("metric is singular")
        inverse = g.inv()
        gamma = [
            [
                [
                    sp.simplify(
                        sum(
                            inverse[i, l]
                            * (
                                sp.diff(g[l, k], coordinates[j])
                                + sp.diff(g[l, j], coordinates[k])
                                - sp.diff(g[j, k], coordinates[l])
                            )
                            for l in range(n)
                        )
                        / 2
                    )
                    for k in range(n)
                ]
                for j in range(n)
            ]
            for i in range(n)
        ]
        ricci = sp.Matrix(
            n,
            n,
            lambda i, j: sp.simplify(
                sum(
                    sp.diff(gamma[k][i][j], coordinates[k])
                    - sp.diff(gamma[k][i][k], coordinates[j])
                    + sum(
                        gamma[k][i][j] * gamma[l][k][l]
                        - gamma[k][i][l] * gamma[l][j][k]
                        for l in range(n)
                    )
                    for k in range(n)
                )
            ),
        )
        result = {
            "determinant": str(determinant),
            "christoffel": [[list(map(str, row)) for row in plane] for plane in gamma],
            "ricci": encode(ricci),
            "scalar_curvature": str(
                sp.simplify(
                    sum(inverse[i, j] * ricci[i, j] for i in range(n) for j in range(n))
                )
            ),
            "scope": "local chart with det(g)!=0; positivity, regularity and completeness are not established",
            "convention": "Ric_ij = d_k Gamma^k_ij - d_j Gamma^k_ik + Gamma^k_ij Gamma^l_kl - Gamma^k_il Gamma^l_jk",
        }
    else:
        raise ValueError("unknown operation")
    result["required_nonzero_denominators"] = sorted({str(v) for v in denominators})
    result["domain_note"] = (
        "Retain input assumptions and function domains; transcendental branch restrictions are not exhaustively inferred."
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
