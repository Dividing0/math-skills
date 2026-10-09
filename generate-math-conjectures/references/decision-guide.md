# Method selection and completion guide

## Task-specific checkpoints

| Checkpoint | Required evidence | If unmet |
|---|---|---|
| 1. Identify the object class, observable property and admissible parameters. State the evidence source and its limitations. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 2. Explore diverse examples, degenerate cases and adversarial families before fitting a pattern. For computations, record algorithms, exact versus floating arithmetic and tested ranges. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 3. Formulate explicit quantifiers and hypotheses. Prefer a falsifiable precise claim over an ambiguous qualitative pattern. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 4. Separate observed regularities, heuristics and proved lemmas. Check known results through primary sources before suggesting novelty. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 5. Search for counterexamples and competing formulations; narrow hypotheses only with a reason and retain a record of failed versions. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |
| 6. Return a conjecture dossier: claim, supporting evidence, attempted falsification, candidate proof approaches and next discriminating experiment. Never treat finite tests as proof of an unbounded claim. | Record the concrete definitions, calculation, source hypothesis or argument that discharges this step. | State the exact unmet obligation; do not silently import an assumption. |

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
