---
name: certify-math-computations
description: "Construct rigorous exact or interval certificates for roots, bounds, identities and finite exhaustive claims. Use when numerical estimates must become checkable proofs with rounding control and explicit coverage."
---

# Certify Math Computations

## Workflow

1. State the mathematical claim, input uncertainty and certification target: enclosure, root isolation, exact identity or finite exhaustive result.
2. Choose exact arithmetic, outward-rounded intervals or a theorem-backed certificate method. Arbitrary precision alone is not a certificate.
3. Control rounding for every relevant operation and library function; justify input enclosures and conversion of decimal data.
4. Generate a certificate and verify it with a simpler independent checker when feasible; record assumptions and coverage.
5. For root isolation, distinguish existence, uniqueness and completeness. Treat intervals containing zero or singularities as unresolved unless a valid method resolves them.
6. Return bounds, certificate, verification procedure and remaining uncertainty; never call a small residual a proof of a nearby unique solution.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.

Read [certificate-tool.md](references/certificate-tool.md) when a univariate rational polynomial needs an exact root bracket. Run the bundled script only for its documented input model and report existence separately from uniqueness.
