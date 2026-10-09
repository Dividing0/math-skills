---
name: research-algebraic-topology
description: "Compute homology, induced maps and fundamental groups of spaces. Use when working with cellular chains, Mayer–Vietoris or van Kampen, auditing equivalence claims, and tracking coefficients, basepoints and torsion."
---

# Research Algebraic Topology

## Workflow

1. Specify spaces, basepoints, coefficients and category assumptions.
2. Distinguish homeomorphism, homotopy equivalence and equality of invariants.
3. Check exact sequences and naturality with explicit maps.
4. Track torsion, coefficient changes and orientation; do not treat one matching invariant as a complete classification.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Runnable helper

Use [simplicial_homology.py](scripts/simplicial_homology.py) to compute unreduced homology dimensions of a finite simplicial complex over F_p. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
