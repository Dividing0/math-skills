---
name: generate-math-conjectures
description: "Form precise falsifiable conjectures from mathematical examples and computational patterns. Use when proposing integer, combinatorial or analytic generalizations, probing counterexamples or separating observation from proof."
---

# Generate Math Conjectures

## Workflow

1. Identify the object class, observable property and admissible parameters. State the evidence source and its limitations.
2. Explore diverse examples, degenerate cases and adversarial families before fitting a pattern. For computations, record algorithms, exact versus floating arithmetic and tested ranges.
3. Formulate explicit quantifiers and hypotheses. Prefer a falsifiable precise claim over an ambiguous qualitative pattern.
4. Separate observed regularities, heuristics and proved lemmas. Check known results through primary sources before suggesting novelty.
5. Search for counterexamples and competing formulations; narrow hypotheses only with a reason and retain a record of failed versions.
6. Return a conjecture dossier: claim, supporting evidence, attempted falsification, candidate proof approaches and next discriminating experiment. Never treat finite tests as proof of an unbounded claim.

## Evidence and output discipline

Maintain a ledger separating given facts, verified external results, proved claims, conjectures and computational observations. State assumptions and unresolved obligations explicitly. Cite external mathematical results with a verifiable source and precise locator when available; do not invent references. Read supplied papers before relying on their contents. Use tools only when they improve verification and state which checks actually ran. Respect the user’s language.

Read [acceptance-cases.md](references/acceptance-cases.md) to check the intended boundary behavior before completing a task. Hand off downstream work with the exact statement, assumptions, evidence and remaining obligations; load other skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Host computation

When the `run-math-python` skill is installed alongside this skill, inventory installed packages and executable paths before selecting a host computation; use the existing execution runner to retain source, commands and actual logs. Use its [host_capabilities.py](../run-math-python/scripts/host_capabilities.py) helper and [input/command reference](../run-math-python/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
