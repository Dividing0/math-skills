---
name: compute-topology-with-gudhi
description: Compute finite simplicial complexes and persistent homology using GUDHI. Use for explicit filtered complexes, Rips or alpha complexes, persistence diagrams, Betti numbers and topology experiments.
---

# Compute Topology with GUDHI

## Workflow
1. Specify the finite complex or point-cloud construction, metric/units, filtration convention, requested homology dimensions and prime coefficient field. Do not identify sampled persistence with the topology of an unknown space without sampling assumptions.
2. Validate finite coordinates or distance matrices, symmetry and nonnegative dissimilarities. Distinguish a valid metric from an arbitrary dissimilarity. Estimate simplex growth before Rips construction; cap scale/dimension and report truncation.
3. For a `SimplexTree`, insert faces with filtration no greater than cofaces and verify monotonicity after edits. If `make_filtration_non_decreasing()` changes input, report the repair rather than silently changing the model.
4. Compute persistence before requesting intervals or Betti numbers. Set prime `homology_coeff_field` explicitly and `persistence_dim_max=True` when the highest represented dimension matters. To determine H_k deaths, include (k+1)-simplices; a one-skeleton cannot detect filled triangles.
5. Preserve infinite deaths explicitly rather than invalid JSON Infinity; state treatment of zero-length bars. Compare small cases against boundary-matrix ranks or Euler characteristic. Transfer assumptions/results to `research-algebraic-topology` or `research-computational-geometry`.

## Execution and handoff
Read [the library playbook](references/library-playbook.md) for the API map, worked example and integration contract. Run `python scripts/example.py --self-test` with the interpreter selected by `run-math-python`; preserve stdout, stderr, exit status and dependency versions. Missing dependencies must produce a failed run, never a fabricated result. Keep the demonstration separate from the user's implementation.

Receive a mathematical statement, assumptions, input schema, target quantity, precision/tolerance and resource budget. Return runnable code, input provenance, versions, diagnostics, measured results, failed checks and limitations. Mark the result as exact on a specified finite object, numerical approximation, Monte Carlo estimate, or unexecuted; never label a computation a universal proof. Hand results to the named mathematical skill for interpretation and to `validate-math-implementation` for implementation checks.
