---
name: quantify-model-uncertainty
description: "Propagate parameter, observation and model uncertainty with explicit dependence assumptions. Use when building deterministic enclosures, probabilistic intervals or simulation-based uncertainty estimates."
---

# Quantify Model Uncertainty

## Workflow

1. Separate measurement noise, uncertain parameters, numerical error and model discrepancy.
2. Specify what interval or probability is requested and the interpretation of its uncertainty.
3. Justify distributions, dependence and priors from evidence; use bounds when probabilities cannot be supported.
4. Choose propagation by sampling, linearization, bounds or surrogate models; verify convergence and approximation error.
5. Distinguish confidence, credible and prediction intervals; validate coverage or calibration under the relevant design.
6. Return assumptions, uncertainty decomposition and decision implications; do not assign unsupported probabilities to unknown quantities.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.

## Host computation

When the `compute-with-numpy` skill is installed alongside this skill, use `propagate-covariance` for a specified linear map and covariance; interpreting a Jacobian this way is a local approximation. Use its [analyze.py](../compute-with-numpy/scripts/analyze.py) helper and [input/command reference](../compute-with-numpy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
