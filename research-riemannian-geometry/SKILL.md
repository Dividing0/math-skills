---
name: research-riemannian-geometry
description: "Compute metric distances, connections and geodesics and assess completeness or curvature-based global results; separate local chart calculations from comparison hypotheses."
---

# Riemannian Geometry

## Workflow

1. Specify the manifold, metric, smoothness and completeness assumptions.
2. Declare curvature sign conventions and normalize comparison quantities.
3. Distinguish geodesic, metric and local completeness claims.
4. Verify hypotheses of comparison, compactness and rigidity theorems.
5. Separate local coordinate computations from global geometric arguments.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `metric` for local Christoffel, Ricci and scalar-curvature calculations in a supplied chart; positivity and global completeness need separate arguments. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
