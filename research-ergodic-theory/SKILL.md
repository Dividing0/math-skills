---
name: research-ergodic-theory
description: "Analyze measure-preserving dynamical systems, invariant measures, ergodicity, mixing and time averages. Use for ergodic theorems and invariant sigma-algebras, distinguishing almost-everywhere conclusions from orbit experiments."
---

# Research Ergodic Theory

## Workflow

1. Specify the measurable space, transformation or flow, invariant measure and observable class. Check finite/probability versus infinite measure and invertibility assumptions before choosing a theorem.
2. Prove measure preservation and identify invariant sets or the invariant sigma-algebra. Ergodicity means invariant sets are null or conull; it is not equivalent to every orbit being dense or to mixing.
3. Match the averaging theorem to the requested mode of convergence and integrability. In a nonergodic system, limiting time averages generally depend on the invariant component rather than equal the global space average.
4. Distinguish ergodicity, weak/strong mixing and quantitative correlation decay. State observables and norms when discussing rates; qualitative theorems alone provide no finite-time error bound.
5. Use exact finite systems and orbit calculations to expose counterexamples, and numerical experiments to investigate specified observables. A long trajectory cannot establish measure-theoretic ergodicity of an infinite system.
6. Report hypotheses, exceptional sets, convergence mode and the scope of each computation. Treat zero-measure components according to almost-everywhere claims rather than counting all displayed orbits equally.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [finite_dynamics.py](scripts/finite_dynamics.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
