---
name: verify-proof-certificates
description: "Verify exact algebraic, optimization or exhaustive proof certificates. Use when checking feasibility, input identity, coverage and checker assumptions while distinguishing invalid from unverifiable outcomes."
---

# Proof Certificate Verification

## Workflow

1. Specify what theorem a certificate purports to establish.
2. Inspect certificate format, input identity and checker assumptions.
3. Verify the checker validates all substantive conditions instead of trusting generator claims.
4. Run the actual checker and record version, exact inputs and result.
5. Distinguish invalid, unverifiable and valid-with-assumptions outcomes.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.

## Runnable helper

Use [check_certificate.py](scripts/check_certificate.py) to check exact rational linear-system and linear-program optimality certificates. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
