#!/usr/bin/env python3
"""Fit a user-supplied full-rank OLS design with conventional or HC3 uncertainty."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("numpy", "statsmodels")
EVIDENCE = "statistical-estimates-conditional-on-model"
EXAMPLE = {
    "design": [[0], [1], [2], [3], [4], [5]],
    "response": [2, 3, 7, 7, 11, 11],
    "covariance": "HC3",
}


def compute(data):
    import numpy as np
    import statsmodels.api as sm

    X, y = (
        np.asarray(data["design"], dtype=float),
        np.asarray(data["response"], dtype=float),
    )
    if (
        X.ndim != 2
        or y.ndim != 1
        or X.shape[0] != len(y)
        or not X.size
        or not np.isfinite(X).all()
        or not np.isfinite(y).all()
    ):
        raise ValueError("design and response must have aligned, finite rows")
    intercept = data.get("intercept", True)
    if type(intercept) is not bool:
        raise TypeError("intercept must be Boolean")
    if intercept:
        X = sm.add_constant(X, has_constant="add")
    if len(y) <= X.shape[1] or np.linalg.matrix_rank(X) != X.shape[1]:
        raise ValueError(
            "design must have full column rank and positive residual degrees of freedom"
        )
    covariance = data.get("covariance", "HC3")
    if covariance not in {"nonrobust", "HC3"}:
        raise ValueError("covariance must be nonrobust or HC3")
    leverage = np.sum(np.linalg.qr(X, mode="reduced")[0] ** 2, axis=1)
    if covariance == "HC3" and np.any(leverage >= 1 - 1e-12):
        raise ValueError("HC3 undefined or unstable at unit leverage")
    alpha = float(data.get("alpha", 0.05))
    if not 0 < alpha < 1:
        raise ValueError("alpha must be between zero and one")
    fit = sm.OLS(y, X, missing="raise").fit(cov_type=covariance)
    intervals = fit.conf_int(alpha=alpha)
    if not np.isfinite(intervals).all():
        raise ValueError(
            "nonfinite coefficient uncertainty; inspect residual variance and design"
        )
    result = {
        "coefficients": fit.params.tolist(),
        "confidence_intervals": intervals.tolist(),
        "covariance": covariance,
        "alpha": alpha,
        "residuals": fit.resid.tolist(),
        "nobs": int(fit.nobs),
        "residual_df": int(fit.df_resid),
        "condition_number": float(np.linalg.cond(X)),
        "normal_equation_residual": float(np.linalg.norm(X.T @ fit.resid)),
        "causal_claim": False,
        "scope": "conditional on the supplied linear model and covariance assumptions",
    }
    if "prediction_design" in data:
        test = np.asarray(data["prediction_design"], dtype=float)
        if test.ndim != 2 or not np.isfinite(test).all():
            raise ValueError("prediction design must be a finite matrix")
        if intercept:
            test = np.column_stack([np.ones(len(test)), test])
        if test.shape[1] != X.shape[1]:
            raise ValueError("prediction columns do not match fitted design")
        result["predictions"] = fit.predict(test).tolist()
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
