# Routing mathematical tasks to executable evidence

Use this table after reading the originating mathematical skill and defining the input domain. Each name identifies a separate companion skill; dispatch only the required companions.

| Mathematical need | Companion | Result and independent checks |
| --- | --- | --- |
| Execution, logs, notebooks | run-math-python | Source hash, versions, actual outputs; exit status is separate from mathematical validation |
| Dense arrays, linear algebra | compute-with-numpy | Shape/dtype checks, rank, residual, analytic small case |
| ODEs, roots, quadrature, sparse systems | compute-with-scipy | Method hypotheses, convergence status, analytic reference |
| Algebraic expressions and exact identities | compute-with-sympy | Exact domains, branches, assumptions and substitution |
| Arbitrary precision experiments | compute-high-precision | Independent reference, precision study; additional digits are not a certificate |
| Rigorous ball arithmetic | certify-with-python-flint | Exact inputs, outward enclosures and inclusion/exclusion predicates |
| Exact algebra and number theory | compute-with-sagemath | Parent/coefficient ring, exact arithmetic, native dependency |
| Graphs and discrete structures | analyze-graphs-with-networkx | Graph type, weights, independent path or combinatorial oracle |
| Statistical estimation | analyze-data-with-statsmodels | Design rank, missingness, model assumptions, uncertainty |
| Bayesian models | infer-with-pymc | Priors, posterior sampling, R-hat/ESS/MCSE/divergences; sampling uncertainty |
| Convex optimization | optimize-with-cvxpy | DCP checks, solver status, recomputed constraints/objective |
| Derivatives and array accelerators | differentiate-with-jax | Dtype, differentiation assumptions, analytic/finite-difference comparison |
| PDE finite elements | solve-pde-with-fenicsx | Weak form, boundary conditions, mesh studies, independent manufactured solution |
| Dynamical systems and control | analyze-systems-with-python-control | Time convention, units, dimensions, poles and independent trajectory |
| Persistent homology | compute-topology-with-gudhi | Filtration, coefficient field, dimension convention, independent boundary ranks |
| Figures and convergence plots | visualize-math-results | Valid domains, axis scales, units and data provenance |

## Shared handoff

Input: original mathematical statement; domain/coefficient ring and hypotheses; data with hashes and units; required result type (exact, approximate, Monte Carlo or enclosure); precision/tolerances; RNG initialization and seed; runtime budget; requested artifacts. Preserve singularities, boundary conditions and quantifiers.

Output: commands, source/hash and all inputs; concrete interpreter and versions; backend/solver configuration; actual stdout/stderr and execution status; result values with units; independent validation and its tolerance; uncertainty or enclosure when justified; unresolved assumptions and proof obligations. Missing dependencies and failed execution must remain visible.

Use formulate-math-problem/build-math-definitions before dispatch if the statement is ambiguous; derive-executable-algorithm for the computational formulation; validate-math-implementation/audit-numerical-methods for validation; reproduce-paper-results for reproduction. Return exact proof obligations to construct-math-proofs/review-math-proofs. Finite examples can help find-math-counterexamples or generate-math-conjectures; they do not establish an unrestricted universal claim.

## Environment preparation

Select one interpreter and create an isolated environment when needed. Install only relevant libraries; record the exact versions actually used. SageMath and FEniCSx require their supported native environments and cannot be replaced by a similarly named pip package. The companion scripts report missing dependencies. Notebook kernels also require an available transport; failure to start a kernel is an execution limitation, not an executed notebook result.
