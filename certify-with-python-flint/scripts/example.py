#!/usr/bin/env python3
if not __debug__:
    raise RuntimeError(
        "Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE."
    )

import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "--self-test",
    action="store_true",
    help="Run independent oracle checks (also run by default)",
)
args = parser.parse_args()
try:
    from fractions import Fraction

    import flint
    from flint import arb, ctx, fmpq, fmpz_poly

    def compute():
        old = ctx.prec
        try:
            ctx.prec = 160
            root = arb(2).sqrt()
            lower = Fraction(7, 5)
            upper = Fraction(3, 2)
            assert lower**2 < 2 < upper**2
            assert root.is_finite()
            assert root > arb(fmpq(7, 5))
            assert root < arb(fmpq(3, 2))
            x = fmpz_poly([0, 1])
            assert (x - 1) * (x + 1) == fmpz_poly([-1, 0, 1])
            assert (root * root).contains(arb(2))
            result = {
                "sqrt2_ball": str(root),
                "bracket": ["7/5", "3/2"],
                "precision_bits": ctx.prec,
                "polynomial": "(x-1)*(x+1)=x^2-1",
                "validation": "validated-enclosure-and-exact-algebra",
                "version": flint.__version__,
            }
        finally:
            ctx.prec = old
        assert ctx.prec == old
        return result

    result = compute()
    result["self_test"] = "passed"
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
except (ArithmeticError, AssertionError, ImportError, RuntimeError, TypeError, ValueError) as exc:
    print(
        json.dumps(
            {"status": "failed", "error_type": type(exc).__name__, "error": str(exc)}
        ),
        file=sys.stderr,
    )
    sys.exit(1)
