# Modeling and empirical methods

Use this family-level guide together with the domain-specific workflow and boundary case. It supplies candidate strategies, not a theorem whose hypotheses may be skipped.

| Method | Choose when | Obligations | If obligations fail |
|---|---|---|---|
| Mechanistic construction | Physical or application assumptions are available | Check units, conservation, positivity and observation model | Separate model validity from solvability |
| Symmetry and identifiability | Data constrain unknown parameters | Find invariant combinations and local versus global ambiguities | More samples of the same observation may not remove structural confounding |
| Experiment or sensor design | Need discriminating data | Check noise, feasible interventions and whether the design breaks ambiguity | Separate precision improvement from identifiability improvement |
| Sensitivity and uncertainty propagation | Need robust decisions | Specify dependence, ranges and model discrepancy | Do not invent distributions or confuse sensitivity with causality |

## Task-specific anchor

Read [acceptance-cases.md](acceptance-cases.md). State which strategy above handles that case, what exact assumption is missing, and what can be concluded after repairing it. Do not assume the repair automatically proves the desired result.
