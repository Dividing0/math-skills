# Optimize with SCIP: playbook

## Worked finite model

The example maximizes `3x + 2y` subject to `2x + y <= 4`, integer `0 <= x <= 10`, and binary `y`. Enumeration gives `(x,y)=(2,0)` with objective 6; the alternative `(1,1)` has objective 5. This supplies an independent small reference for the model and objective sense.

The helper handles linear continuous/integer/binary models. A task-specific nonlinear model can use PySCIPOpt expression APIs after checking their installed support. Do not call a continuous relaxation's solution an integer-feasible incumbent.

## Acceptance cases

- Time limit with a solution: return the incumbent, bound and gap with the limit status.
- Infeasible model: do not call solution accessors requiring an incumbent.
- Binary variable relaxed to continuous: show the changed feasible set.
- Large feasibility or integrality residual: flag the returned candidate despite a favorable status.
- Infinite/unavailable bound: use an explicit absent value, not a finite certificate.

## Primary sources

[PySCIPOpt tutorials](https://pyscipopt.readthedocs.io/en/latest/tutorials/) and [SCIP problem classes](https://www.scipopt.org/doc/html/WHATPROBLEMS.php).
