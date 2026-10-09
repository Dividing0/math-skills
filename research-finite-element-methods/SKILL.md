---
name: research-finite-element-methods
description: "Derive and audit finite element weak forms, Galerkin spaces, coercivity, mixed inf-sup stability, assembly and approximation errors under explicit mesh and regularity assumptions."
---

# Метод скінченних елементів

## Workflow

1. Specify PDE, weak form, function spaces and boundary conditions.
2. Choose conforming or nonconforming spaces and mesh assumptions.
3. Verify coercivity or inf-sup stability and consistency.
4. Separate approximation, quadrature, linear-solver and rounding errors.
5. Check convergence with manufactured solutions and mesh refinement without replacing theoretical hypotheses.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.

## Host computation

When the `research-numerical-analysis` skill is installed alongside this skill, inspect an independently generated mesh/error table for observed convergence orders; a refinement table is not a PDE convergence or regularity theorem. Use its [refinement.py](../research-numerical-analysis/scripts/refinement.py) helper and [input/command reference](../research-numerical-analysis/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
