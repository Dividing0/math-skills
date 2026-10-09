---
name: research-mathematical-logic
description: "Analyze syntax, models, formal derivability and computability. Use for validity or satisfiability, countermodels, capture-free substitution, proof-system hypotheses and metatheoretic independence arguments."
---

# Research Mathematical Logic

## Workflow

1. Specify syntax, semantics, logic and axioms.
2. Distinguish provability, truth in a model, validity and satisfiability.
3. Track variable binding and capture-free substitution.
4. State effectiveness and encoding assumptions for computability or incompleteness arguments; avoid transferring classical principles to constructive settings.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.

## Runnable helper

Use [truth_table.py](scripts/truth_table.py) to exhaustively check a classical propositional formula encoded as a JSON tree. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.

## Related workflow

For executable SMT encodings, models and conflicting assertion sets, use the Z3 workflow; preserve the intended sorts and distinguish unknown from unsatisfiable. Read [solve-with-z3](../solve-with-z3/SKILL.md) when that specialization is needed and available.
