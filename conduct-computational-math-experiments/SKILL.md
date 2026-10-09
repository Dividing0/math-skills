---
name: conduct-computational-math-experiments
description: "Design reproducible exact or numerical experiments for mathematical claims. Use when enumerating finite objects, sampling conjectures, testing adversarial cases or auditing computational evidence and coverage."
---

# Conduct Computational Math Experiments

## Workflow

1. State the conjecture, domain, observable, falsification criterion and computational budget.
2. Choose systematic enumeration, randomized sampling or structured adversarial examples; explain coverage and selection bias.
3. Specify exact or floating arithmetic, precision, seeds, stopping rules and software versions.
4. Validate the experiment on known cases and an independent formulation; test overflow, cancellation and boundary conditions.
5. Preserve code, parameters and machine-readable results; separate discovery samples from subsequent validation.
6. Report tested ranges, failures, sensitivity and computational observations without promoting finite evidence to an unrestricted proof.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Host computation

When the `run-math-python` skill is installed alongside this skill, inventory installed packages and executable paths before selecting a host computation; use the existing execution runner to retain source, commands and actual logs. Use its [host_capabilities.py](../run-math-python/scripts/host_capabilities.py) helper and [input/command reference](../run-math-python/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.

For an actual experiment script, use the adjacent [run_math.py](../run-math-python/scripts/run_math.py) runner with `--script /absolute/experiment.py --out /new/output/directory --timeout 60 -- --input /absolute/request.json`. It records the executed source, environment, stdout/stderr and exit status. Use an interpreter containing the script's required packages; the seed recorded by the runner does not automatically seed the experiment.

## Related workflow

For sampling-based estimates, use the Monte Carlo workflow to define independent units, quantify sampling error and document variance reduction. Read [compute-with-monte-carlo](../compute-with-monte-carlo/SKILL.md) when that specialization is needed and available.
