# Library playbook

## API selection
`pm.Model`, `pm.Beta`, `pm.Binomial`, `pm.NUTS`, `pm.sample`, `az.summary`, `az.rhat`, `az.ess`, `az.mcse`; specify `step=pm.NUTS(target_accept=0.9)` for a clear PyMC sampler across supported signatures.

Use installed-version API documentation when signatures differ. Official references checked on 2026-10-08:
- https://www.pymc.io/projects/docs/en/stable/api/generated/pymc.sample.html
- https://www.pymc.io/projects/docs/en/stable/pymc-examples/examples/getting_started.html
- https://python.arviz.org/projects/stats/en/latest/api/index.html

## Worked computation
With Beta(2,3) prior and 6 successes in 10 independent trials, conjugacy gives Beta(8,7), mean8/15 and variance56/(225·16). The script executes a small two-chain NUTS run, compares its mean against the exact mean with a loose smoke tolerance and reports diagnostics. The analytic benchmark is exact; samples remain approximate.

Execute [the demonstration](../scripts/example.py) with `--self-test`; it emits JSON and raises on failed independent checks. Default execution performs the same calculation; `--self-test` additionally validates known failure cases when provided.

## Wrong inference
No divergences and a plausible sample mean do not certify posterior convergence, and a posterior interval is conditional on likelihood and prior. This smoke budget cannot validate an arbitrary hierarchical model.

## Integration contract
Input: problem statement, mathematical assumptions, serialized data or provenance, target quantity, domain/support or graph/complex semantics, tolerance, resource budget. Obtain missing essential semantics before computing.
Output: actual execution status; Python and library versions; method and options; result with units and object semantics; checks, diagnostics and warnings; code/artifact paths. Explicitly distinguish exact arithmetic, floating estimates and Monte Carlo estimates. Do not substitute stdout for mathematical validation. Route unsupported requirements back to the originating mathematical skill and preserve open obligations.

## Dependency failures
Import the required package in the selected interpreter. If absent, return nonzero status with a dependency message; do not create an output labeled successful. Environment preparation belongs to `run-math-python`, and skill creation never implies dependency installation.

Official configuration reference: https://pytensor.readthedocs.io/en/latest/library/config.html (checked 2026-10-08).

## Portable execution backend
The bundled small smoke run explicitly sets `pytensor.config.cxx=""` to use a portable Python execution path and reports this backend in JSON. This avoids relying on a system Python development shared library. It is slower and is not a performance recommendation. If compiled execution fails, retain compiler diagnostics and explicitly choose a compatible backend rather than claiming the original run succeeded. Production inference should use a prepared compiled environment or a deliberately selected supported backend.
