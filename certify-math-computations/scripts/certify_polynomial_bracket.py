#!/usr/bin/env python3
"""Exact rational certificate for a univariate rational polynomial on [a,b].
Coefficients are constant-first. No floating point or numerical root assumptions.
"""

import argparse
import json
from fractions import Fraction as Q


def value(coefficients, x):
    result = Q(0)
    for c in reversed(coefficients):
        result = result * x + c
    return result


def interval_value(coefficients, a, b):
    lo = hi = Q(0)
    for c in reversed(coefficients):
        terms = [lo * a, lo * b, hi * a, hi * b]
        lo, hi = min(terms) + c, max(terms) + c
    return lo, hi


def certify(coefficients, a, b, steps=32):
    raw = list(coefficients)
    if any(isinstance(c, float) for c in raw + [a, b]):
        raise ValueError(
            "Pass exact rational strings, integers or Fraction values, not binary floats"
        )
    cs = [Q(c) for c in raw]
    a, b = Q(a), Q(b)
    if not cs:
        raise ValueError("At least one coefficient is required")
    if a >= b:
        raise ValueError("Require a < b")
    if not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    left, right = a, b
    fa, fb = value(cs, a), value(cs, b)
    if fa * fb > 0:
        raise ValueError(
            "No endpoint sign-change certificate; this does not prove absence of roots"
        )
    derivative = [i * cs[i] for i in range(1, len(cs))]
    dlo, dhi = interval_value(derivative, a, b)
    unique = dlo > 0 or dhi < 0
    if fa == 0:
        left = right = a
    elif fb == 0:
        left = right = b
    else:
        for _ in range(steps):
            mid = (left + right) / 2
            fm = value(cs, mid)
            if fm == 0:
                left = right = mid
                break
            if fa * fm < 0:
                right = mid
            else:
                left = mid
                fa = fm
    return {
        "coefficients": [str(c) for c in cs],
        "original_interval": [str(a), str(b)],
        "original_endpoint_values": [str(value(cs, a)), str(value(cs, b))],
        "root_enclosure": [str(left), str(right)],
        "derivative_enclosure": [str(dlo), str(dhi)],
        "existence_certified": True,
        "uniqueness_on_original_interval_certified": unique,
        "arithmetic": "exact rational",
        "method": "continuity + endpoint signs; strict derivative sign for uniqueness",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--coefficients",
        nargs="+",
        required=True,
        help="constant-first rational strings",
    )
    parser.add_argument("--left", required=True)
    parser.add_argument("--right", required=True)
    parser.add_argument("--steps", type=int, default=32)
    args = parser.parse_args()
    try:
        print(
            json.dumps(
                certify(args.coefficients, args.left, args.right, args.steps), indent=2
            )
        )
    except (ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
