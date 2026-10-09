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
    import sympy as sp

    def compute():
        x = sp.Symbol("x", real=True)
        numerator = x**2 - 1
        denominator = x - 1
        original = numerator / denominator
        reduced = sp.cancel(original)
        candidates = sp.solveset(reduced - 2, x, domain=sp.S.Reals)
        excluded = sp.solveset(denominator, x, domain=sp.S.Reals)
        solutions = candidates - excluded
        assert reduced == x + 1
        assert original.subs(x, 0) == sp.Integer(1)
        assert excluded == sp.FiniteSet(1)
        assert solutions == sp.S.EmptySet
        assert sp.sqrt(x**2) == sp.Abs(x)
        return {
            "original": str(original),
            "reduced": str(reduced),
            "excluded": str(excluded),
            "solutions_f_eq_2": str(solutions),
            "validation": "exact-domain-filtered",
            "version": sp.__version__,
        }

    result = compute()
    result["self_test"] = "passed"
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
except Exception as exc:
    print(
        json.dumps(
            {"status": "failed", "error_type": type(exc).__name__, "error": str(exc)}
        ),
        file=sys.stderr,
    )
    sys.exit(1)
