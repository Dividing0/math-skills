# Mechanisms, feasible states and observed quantities

## Choose a branch
- Population dynamics: specify units and nonnegative initial states, then check vector-field direction on each boundary face. A model that exits its feasible region requires correction or an explicitly different interpretation.
- Compartmental conservation: write all transfer rates and sum equations to identify conserved totals or external fluxes. Threshold and equilibrium claims must specify population normalization, parameter signs and the observation model.
- Parameter inference: distinguish state trajectories from measured outputs. Structural identifiability asks whether perfect continuous output determines parameters; a good finite-data fit does not answer that question. Practical uncertainty requires noise and sampling assumptions.

## Worked logistic dynamics
Let N'=rN(1-N/K), r,K>0 and N(0)=N0>0. Separation, or substitution, gives N(t)=K/[1+(K/N0-1)e^(-rt)] for t>=0. The denominator stays positive: when N0>K its lower bound is K/N0, and when N0<=K it is at least one. Thus N remains positive, approaches K, and is monotone toward K. Linearization at K has derivative -r, establishing local asymptotic stability; the explicit formula additionally establishes convergence from every positive initial value.

## Tempting inference and counterexample
A population curve need not identify every mechanistic parameter. If N'= (b-d)N and only N(t) is observed, (b,d)=(3,1) and (4,2) both produce N0 e^(2t). The output identifies b-d under ideal observations, not b and d separately. More time points of the same output do not remove this structural ambiguity.

## Stop or hand off
If units or measured quantities are unspecified, return the mathematically feasible model and explicit interpretation alternatives rather than an empirical assertion. Send indistinguishable parameter families to measurement design with the proposed additional observations. For biological validation require independent data and a named prediction target. Hand simulations the invariant region and event conditions; a numerical trajectory staying nonnegative does not prove invariant feasibility. Keep model-derived thresholds separate from evidence that the assumed mechanism describes the organism or population.
