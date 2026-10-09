---
name: research-spectral-graph-theory
description: "Analyze graph Laplacians, eigenvalues, connectivity and spectral relaxations. Use when checking weight signs, normalization, isolated vertices and rounding from spectral to discrete solutions."
---

# Spectral Graph Theory

## Workflow

1. Specify directedness, weights and the Laplacian or normalized operator convention.
2. Check symmetry, positivity and treatment of isolated vertices.
3. Relate eigenvectors and eigenvalues to connectivity using applicable hypotheses.
4. Distinguish spectral relaxations from exact combinatorial optima.
5. Track multiplicities, normalization and rounding in algorithms derived from spectral results.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.

## Host computation

When the `compute-with-numpy` skill is installed alongside this skill, use `matrix` for a supplied finite discretization or sampled matrix; finite spectral diagnostics do not establish infinite-dimensional operator claims or asymptotic ensemble laws. Use its [analyze.py](../compute-with-numpy/scripts/analyze.py) helper and [input/command reference](../compute-with-numpy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
