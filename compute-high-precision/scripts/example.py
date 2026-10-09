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
    import mpmath
    from mpmath import mp

    def compute():
        ladder = []
        for p in (30, 60, 100):
            with mp.workdps(p):
                h = mp.mpf("1e-40")
                direct = mp.sqrt(1 + h) - 1
                stable = h / (mp.sqrt(1 + h) + 1)
                ladder.append(
                    {
                        "dps": p,
                        "direct": mp.nstr(direct, p),
                        "stable": mp.nstr(stable, p),
                        "relative_difference": mp.nstr(
                            abs(direct - stable) / stable, 12
                        ),
                    }
                )
        with mp.workdps(100):
            h = mp.mpf("1e-40")
            d = mp.sqrt(1 + h) - 1
            s = h / (mp.sqrt(1 + h) + 1)
            assert abs(d - s) / s < mp.mpf("1e-58")
            assert abs(s / (h / 2) - 1) < mp.mpf("1e-39")
            assert abs(s * (s + 2) - h) < mp.mpf("1e-135")
        return {
            "precision_ladder": ladder,
            "validation": "numerical-evidence-not-certified",
            "version": mpmath.__version__,
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
