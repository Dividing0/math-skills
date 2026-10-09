---
name: certify-with-python-flint
description: Use python-flint for exact integer/rational algebra and Arb/Acb validated ball arithmetic. Use when mathematical skills require reproducible enclosures, exact polynomial checks or certified inequality evidence rather than ordinary numerical approximations.
---

# Certify with python-flint

## Workflow

1. State the exact proposition and uncertainty in inputs. Choose `fmpz`/`fmpq` and their polynomial types for exact algebra, `arb` for real balls and `acb` for complex balls. Use exact integer/rational/string input or explicit input balls; avoid treating uncertain floats as exact measurements.
2. Set `ctx.prec` (bits) or `ctx.dps` (digits), record it and restore the previous setting in `finally`. Rebuild the computation at higher precision if balls overlap decision thresholds; precision cannot eliminate genuine input uncertainty.
3. Preserve full ball radii when exporting `str`; record finite status. Never certify from midpoints or strings with `radius=False`. Check installed API signatures against linked docs when changing a routine.
4. Evaluate only supported validated operations across their defined domains. A denominator ball containing zero, real sqrt across negatives or unresolved branch creates an inconclusive/invalid calculation; use subdivisions or complex analysis with explicit branches where justified.
5. Interpret comparisons as separation evidence; overlapping balls are inconclusive. `r.contains(0)` says evaluation could be zero, not that a root exists. To establish root existence/uniqueness use a stated theorem (sign change with continuity, interval Newton/Krawczyk with hypotheses) and independently check its obligations.
6. Build certificate records with exact inputs, precision, operation chain, returned balls and theorem obligations. Cross-check exact polynomial results with direct algebra or exact integer arithmetic. A library enclosure is computational evidence for the stated proposition, not a proof-assistant-checked theorem.
7. Hand off bounded computations to `certify-math-computations`, `design-computer-assisted-proofs` and `verify-proof-certificates`; let `review-math-proofs` assess the inference from enclosure to theorem. Use `run-math-python` for execution provenance.

## Resources

Read [library-playbook](references/library-playbook.md) for the worked example, failure analysis, API sources and inter-skill contract. Run [example.py](scripts/example.py) with `--self-test` as the dependency smoke check; assertions run even without the flag. Report dependency failures rather than simulated results.
