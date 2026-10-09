---
name: research-operator-theory
description: "Analyze bounded or unbounded operators, adjoints, compactness and spectra on Banach or Hilbert spaces. Use when checking domains, invertibility, spectral components or self-adjointness."
---

# Теорія операторів

## Workflow

1. Specify the Banach or Hilbert space, operator domain and scalar field.
2. Distinguish boundedness, closedness, self-adjointness and symmetry.
3. Track point, continuous and residual spectrum in the appropriate setting.
4. Verify compactness or normality before spectral decompositions.
5. Check domains of products and adjoints; finite matrix intuition does not settle infinite-dimensional spectra.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.

## Host computation

When the `compute-with-numpy` skill is installed alongside this skill, use `matrix` for a supplied finite discretization or sampled matrix; finite spectral diagnostics do not establish infinite-dimensional operator claims or asymptotic ensemble laws. Use its [analyze.py](../compute-with-numpy/scripts/analyze.py) helper and [input/command reference](../compute-with-numpy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
