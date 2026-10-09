---
name: solve-inverse-problems
description: "Recover states or parameters through forward operators, regularization and stability analysis. Use when checking singular/null directions, Tikhonov/SVD methods, bias and local versus global identifiability."
---

# Solve Inverse Problems

## Workflow

1. Define the forward operator, observation process, noise assumptions and target unknown.
2. Analyze existence, uniqueness and stability; identify null spaces and inaccessible modes.
3. Choose a regularizer or prior aligned with domain information; explain the bias introduced.
4. Select its strength using a justified procedure without leaking validation data; scale operators and variables.
5. Check residuals, uncertainty and sensitivity to noise, initialization and regularization; compare with a simple baseline.
6. Return recovery, resolvable features and limitations. Distinguish numerical convergence from recovery of the true unknown.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Host computation

When the `compute-with-numpy` skill is installed alongside this skill, use `tikhonov` or `least-squares` for a supplied finite forward matrix and data; report residuals, numerical rank and regularization bias. Use its [analyze.py](../compute-with-numpy/scripts/analyze.py) helper and [input/command reference](../compute-with-numpy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
