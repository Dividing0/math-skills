# Experiments that can be reproduced and falsified

## Choose a branch
- Exhaustive finite enumeration: define a complete generator, remove duplicates only with a proved equivalence, and count the domain independently. Exact arithmetic is preferable when the predicate is discrete. Completeness establishes only the advertised finite range.
- Random sampling: record the sampling distribution, seed, draws and exclusions. A binomial uncertainty calculation requires independent identically distributed trials of a fixed event; adaptive sampling needs a different analysis.
- Adversarial numerical exploration: include near-singular, large-magnitude and cancellation cases. Compare an independent formula at higher precision or exact arithmetic, rather than rerunning the same unstable formula.

## Worked protocol
Test whether squares of integers 0 through 9 are congruent to 0 or 1 modulo 4. Enumerate n with integer arithmetic and record (n,n² mod 4). The ten residues alternate 0,1. A separate parity proof checks the experiment: n=2k gives n²=4k², while n=2k+1 gives n²=4k(k+1)+1. Here the unrestricted conclusion comes from this argument, not from ten observations. The finite table is an implementation check and should be preserved with its exact tested interval.

## Tempting inference and counterexample
An experiment using machine arithmetic can falsify its own implementation rather than the conjecture. In binary64, the mathematical expression (10^16+1)-10^16 evaluates to 0 under ordinary rounded addition, although exact arithmetic gives 1. Agreement between two code paths using that same intermediate addition is not independent confirmation. Retain raw inputs and rerun disputed witnesses with exact arithmetic before reporting a mathematical failure.

## Stop or hand off
If a generator's coverage is unproved, report sampled coverage and leave completeness open. If a putative witness depends on rounding, pass the exact input and precision history to computation certification. Deliver code, environment, seeds, stopping rule, raw outputs, independent controls and failures. Describe wall-clock or memory termination as resource limits rather than a mathematical stopping theorem. Keep discovery data separate from new validation data and never imply a run occurred when no tool executed it.
