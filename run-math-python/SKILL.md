---
name: run-math-python
description: Execute authorized mathematical Python scripts or Jupyter notebooks in
  an explicit environment; capture source, versions, seed, logs, artifacts and failure
  status. Use when another math skill needs actual computed evidence, reproducible
  experiment output or notebook execution.
---

# Run Math Python

## Workflow

1. Receive an exact task statement, inputs and domains, required libraries, requested numerical precision, runtime budget and output contract. Determine whether the target is an exact identity, numerical approximation, Monte Carlo estimate or rigorous enclosure; running a script does not establish that classification by itself.
2. Select a concrete interpreter. Check its packages and versions; use an isolated project environment for missing dependencies. Preserve dependency locks and external data hashes. Do not silently change a project's environment or substitute another library without recording the effect.
3. Inspect the generated code against mathematical hypotheses and library APIs. Use absolute paths for input data. Require explicit local RNG initialization; MATH_EXPERIMENT_SEED is a recorded input, not automatic seeding. Keep a source snapshot, tolerances, solver settings, hardware/backend and threading settings.
4. Read [execution-playbook.md](references/execution-playbook.md), and [routing.md](references/routing.md), then use scripts/run_math.py for scripts. Supply a new output directory, timeout and package names. For notebooks use the documented explicit interpreter kernel; do not execute through an arbitrary default kernel. Bound a process and report incomplete runs honestly.
5. Inspect return code, stdout and stderr before interpreting results. Require finite values and task-specific residual, analytic oracle, independent small implementation or enclosure checks. Report solver failure, missing dependency, timeout and unverifiable certificate distinctly. Repeat only when a changed method, precision or failure justifies it.
6. Return source and its hash, command, interpreter/package versions, seed handling, logs, numerical result, validation outcomes and generated artifacts. Handoff the original statement and assumptions with unresolved proof obligations. Record precision studies as empirical unless a theorem and arithmetic establish bounds.

## Completion

Use [notebook_example.py](scripts/notebook_example.py) for the explicit-interpreter notebook smoke example; retain kernel startup failures as failures, separately from script checks.

Preserve exact assumptions and distinguish planned code from an actual run. Do not invent solver outputs or dependency availability. Use the user’s language. Read the linked playbook for detailed gates and report which result checks actually ran.
