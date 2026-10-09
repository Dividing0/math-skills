---
name: research-representation-theory
description: "Analyze group/algebra representations, invariant subspaces, characters and intertwiners. Use when decomposing modules or checking scalar-field, characteristic and semisimplicity hypotheses."
---

# Research Representation Theory

## Workflow

1. Specify the group or algebra, scalar field, characteristic and representation class.
2. Distinguish irreducible from indecomposable and finite from infinite-dimensional representations.
3. Check semisimplicity hypotheses before decomposing; construct intertwiners and invariant subspaces.
4. Use character methods only in an appropriate setting and state normalization.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `matrix` for exact finite matrix rank/nullspace or `groebner` for rational polynomial ideal reductions; retain the field, parameter and theorem hypotheses. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
