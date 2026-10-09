#!/usr/bin/env python3
"""OLS + HC3, checked independently by centered sums."""

if not __debug__:
    raise RuntimeError(
        "Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE."
    )

import argparse
import json
import platform
import sys

p = argparse.ArgumentParser()
p.add_argument("--self-test", action="store_true")
args = p.parse_args()
try:
    import numpy as np
    import statsmodels
    import statsmodels.api as sm
    from statsmodels.tools.sm_exceptions import MissingDataError
except ImportError as exc:
    print(
        json.dumps(
            {
                "status": "dependency_missing",
                "dependency": "numpy/statsmodels",
                "error": str(exc),
            }
        ),
        file=sys.stderr,
    )
    sys.exit(2)
x = np.arange(6, dtype=float)
y = np.array([2, 3, 7, 7, 11, 11], dtype=float)
X = sm.add_constant(x, has_constant="add")
assert np.linalg.matrix_rank(X) == X.shape[1]
fit = sm.OLS(y, X, missing="raise").fit(cov_type="HC3")
xb = sum(x) / len(x)
yb = sum(y) / len(y)
slope = sum((float(a) - xb) * (float(b) - yb) for a, b in zip(x, y)) / sum(
    (float(a) - xb) ** 2 for a in x
)
reference = np.array([yb - slope * xb, slope])
assert np.allclose(fit.params, reference, atol=1e-12, rtol=1e-12)
assert np.allclose(X.T @ fit.resid, 0, atol=1e-11)
assert fit.conf_int().shape == (2, 2) and np.isfinite(fit.conf_int()).all()
checks = [
    "centered_sum_coefficients",
    "normal_equation_residual",
    "finite_HC3_intervals",
]
if args.self_test:
    bad = y.copy()
    bad[0] = np.nan
    try:
        sm.OLS(bad, X, missing="raise")
    except MissingDataError:
        checks.append("missing_response_rejected")
    else:
        raise AssertionError("missing response accepted")
    rank_deficient = np.column_stack([np.ones(6), x, 2 * x])
    assert np.linalg.matrix_rank(rank_deficient) == 2
    checks.append("rank_deficiency_detected")
print(
    json.dumps(
        {
            "status": "passed",
            "claim_status": "numerical_estimates_conditional_on_model",
            "python": platform.python_version(),
            "numpy": np.__version__,
            "statsmodels": statsmodels.__version__,
            "coefficients": fit.params.tolist(),
            "HC3_confidence_intervals": fit.conf_int().tolist(),
            "checks": checks,
            "causal_claim": False,
        }
    )
)
