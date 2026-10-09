---
name: solve-differential-algebraic-equations
description: "Analyze and solve DAEs with explicit algebraic constraints, consistent initialization, index assumptions and residual checks. Use for constrained dynamical systems where an ordinary explicit ODE formulation is insufficient."
---

# Solve Differential-Algebraic Equations

## Workflow

1. Write the residual system F(t,y,y_prime)=0 and identify differential/algebraic variables, constraints and initial conditions. State the intended index notion and avoid treating a singular mass matrix as an ordinary invertible ODE mass matrix.
2. Check consistent initialization. In semi-explicit index-one systems, verify the algebraic Jacobian is locally invertible; higher-index or singular cases require additional analysis rather than silent regularization.
3. Choose a DAE-capable method or justify elimination. For the linear helper, constant invertible D permits exact algebraic elimination before backward Euler; this restricted model does not establish solvability for nonlinear/higher-index DAEs.
4. Solve with recorded tolerances, initial derivatives and solver diagnostics. Monitor algebraic constraint residuals and differential residuals using the correct time discretization; a small constraint residual alone does not establish trajectory accuracy.
5. Perform a refinement study against an analytic or independently justified reference. Account for stiffness, conditioning and constraint drift. Differentiating a constraint can introduce solutions that violate the original initial constraint.
6. Return the model, index/regularity assumptions, initialization result, trajectory error evidence and unresolved conditions. If a specialized runtime is unavailable, report the blocker rather than substitute an inequivalent explicit solver.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [linear_dae.py](scripts/linear_dae.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
