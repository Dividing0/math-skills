---
name: research-number-theory
description: "Solve and audit divisibility, congruence, CRT and integer-solvability problems using exact arithmetic. Use when checking modular division, local obstructions or primality evidence."
---

# Research Number Theory

## Workflow

1. Specify integer domains, signs and positivity restrictions.
2. Track divisibility, gcd and modular invertibility before manipulating congruences.
3. Distinguish necessary local congruence conditions from global solvability.
4. For computation use exact arithmetic and distinguish probable-prime tests from primality certificates.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.

## Runnable helper

Use [integer_tools.py](scripts/integer_tools.py) to compute exact generalized CRT solutions and Bezout witnesses. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.

## Related workflow

For number-theoretic cryptographic constructions, use the cryptography workflow to state correctness, security experiments, hardness assumptions and reduction losses separately. Read [research-mathematical-cryptography](../research-mathematical-cryptography/SKILL.md) when that specialization is needed and available.
