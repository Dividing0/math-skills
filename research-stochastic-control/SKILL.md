---
name: research-stochastic-control
description: "Analyze decisions under stochastic dynamics using admissible policies, Bellman equations, finite MDPs and continuous-time verification conditions. Use for stochastic optimal control, separating known-model finite solutions from partial-observation or infinite-horizon claims."
---

# Research Stochastic Control

## Workflow

1. Define the state, actions, transition/noise law, information filtration, costs, horizon and policy class. Require nonanticipativity: an action cannot depend on future noise unavailable to the controller.
2. State the objective and admissibility conditions, including integrability and constraints. Distinguish fully observed Markov control from partial observation and distinguish expected cost from risk-sensitive or chance-constrained criteria.
3. Use dynamic programming only after identifying an adequate state and conditions for conditional optimization/measurable policy selection. Track terminal/boundary conditions and the discount convention.
4. For finite models, compute Bellman recursions and verify action choices and transition normalization. For continuous-time HJB arguments, supply regularity or viscosity framework plus a verification theorem; a formal HJB solution alone is not an optimal policy proof.
5. For numerical/learned policies, separate discretization, approximation, model estimation and Monte Carlo error. Check the policy against the original information structure and constraints, not only the surrogate dynamics.
6. Report policy, value, comparator, assumptions and actual verification. The exact finite-horizon helper supplies a finite known-model result; it does not solve POMDPs, prove infinite-horizon convergence or validate a learned transition model.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [finite_horizon_mdp.py](scripts/finite_horizon_mdp.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
