---
name: research-wavelet-analysis
description: "Analyze Haar and other wavelet transforms, frames, reconstruction and coefficient approximation. Use when verifying normalization, orthogonality, boundary conventions, vanishing moments or thresholding error."
---

# Wavelet Analysis

## Workflow

1. Specify function space, wavelet family and normalization.
2. Verify orthogonality, biorthogonality or frame bounds and reconstruction assumptions.
3. Track vanishing moments, regularity and boundary extension.
4. Distinguish continuous mathematical transforms from finite sampled implementations.
5. Check thresholding bias and approximation error; sparsity claims require a signal class.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Runnable helper

Use [signal_transforms.py](scripts/signal_transforms.py) to compute finite orthonormal Haar or discrete Fourier transforms with reconstruction diagnostics. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
