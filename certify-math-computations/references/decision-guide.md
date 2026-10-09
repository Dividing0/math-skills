# Method selection and completion guide

## Task-specific checkpoints

| Checkpoint | Required evidence | If unmet |
|---|---|---|
| 1. State the mathematical claim, input uncertainty and certification target: enclosure, root isolation, exact identity or finite exhaustive result. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 2. Choose exact arithmetic, outward-rounded intervals or a theorem-backed certificate method. Arbitrary precision alone is not a certificate. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 3. Control rounding for every relevant operation and library function; justify input enclosures and conversion of decimal data. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 4. Generate a certificate and verify it with a simpler independent checker when feasible; record assumptions and coverage. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 5. For root isolation, distinguish existence, uniqueness and completeness. Treat intervals containing zero or singularities as unresolved unless a valid method resolves them. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 6. Return bounds, certificate, verification procedure and remaining uncertainty; never call a small residual a proof of a nearby unique solution. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |

## Choose an appropriate result type

- For an exact claim, construct an argument covering its full quantified domain; finite tests can discover failures but do not replace the argument.
- For an approximation, state the norm, parameter regime and which errors the bound covers; separate arithmetic error from model and truncation error.
- For a computation, choose exact arithmetic or certified enclosures when the conclusion requires rigor; ordinary floating-point results remain numerical evidence.
- For an external theorem, compare its exact assumptions with the present objects before using it.
- For unavailable data, sources or tools, return the strongest supported partial result and an explicit remaining obligation.

## Output contract

Return the exact task and assumptions; selected method and reason; evidence or proof; boundary cases; status of every decisive claim; and next action for unresolved obligations. Keep the report proportional to the task. Do not add an unnecessary full dossier for a simple question.

## Additional behavioral cases

1. **Supported case:** Apply the workflow to a valid task in this area; justify every decisive step.
2. **Removed hypothesis:** Revisit the bundled boundary case with its missing assumption repaired. Explain which step becomes valid and whether the repaired conclusion actually follows.
3. **Alternative formulation:** Give an equivalent formulation if possible, verify both directions, and preserve domain restrictions.
4. **Insufficient evidence:** Repeat the task with decisive input, source or checker unavailable. Return a scoped partial answer rather than fabricated certainty.

These are acceptance templates, not a held-out benchmark. For independent evaluation, create fresh inputs with private rubrics and do not reveal the expected answer to the solving agent.
