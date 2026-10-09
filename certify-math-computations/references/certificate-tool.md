# Exact polynomial bracket certificate

Use `scripts/certify_polynomial_bracket.py` for a univariate polynomial with **exact rational coefficients** on an exact rational closed interval. Coefficients are ordered from the constant term upwards. Interpret a supplied decimal as its exact decimal value only when that is the intended input model; this tool does not propagate measurement uncertainty.

Example:

```bash
python3 scripts/certify_polynomial_bracket.py --coefficients -2 0 1 --left 1 --right 2 --steps 32
```

The certificate records the input polynomial, endpoint values, refined enclosure and an interval enclosure of its derivative. Continuity plus an endpoint root or opposite signs establishes existence. A strictly positive or strictly negative derivative enclosure on the original interval establishes uniqueness there. `false` for uniqueness means **this sufficient criterion did not establish uniqueness**, not that multiple roots exist. A same-sign rejection is inconclusive about root absence. No claim covers roots outside the supplied interval.

Review the certificate independently: check endpoint substitutions exactly; verify the refined interval stays inside the original; derive a derivative bound by rational inequalities. Rational interval Horner evaluation may overestimate, so it can leave a genuinely monotone polynomial unresolved. Exact arithmetic removes rounding error for these operations, but the mathematical proof and implementation still require review. This is not a general proof assistant or an exhaustive root-isolation algorithm.

The callable `certify` API rejects binary floating point inputs. Use integers, rational strings or `Fraction` values. Return the executed command and actual JSON outcome only after running it; otherwise provide a proposed certificate procedure.
