# Research Ergodic Theory: playbook

## Finite model and counterexample

For a permutation of a finite probability space, invariance requires equal point weights along each cycle. The system is ergodic exactly when one cycle has positive measure. On such a cycle, each orbit average is the cycle average. A nontrivial cycle is periodic and not mixing: indicator correlations recur instead of approaching the product of means.

The helper computes cycles and exact rational averages. A swap of two equally weighted states is ergodic but not mixing. The identity on two positive-mass points is not ergodic. A single supported fixed point is mixing, even if zero-mass cycles are also displayed.

For general spaces, Birkhoff-type pointwise results and mean-ergodic Hilbert-space results have different assumptions and conclusions. Record the exact theorem and its invariant projection/conditional expectation, rather than replacing all limits with a constant.

## Acceptance cases

- Invariance fails for supplied weights: do not classify the weighted system using an ergodic theorem.
- One finite cycle of length greater than one: ergodic does not imply mixing.
- Observable happens to have the right average on one orbit: do not infer ergodicity.
- Infinite measure: do not apply a probability-space conclusion unchanged.
- Zero-mass cycles: keep topological orbit information separate from measure-theoretic classification.

## Primary sources

[Terence Tao, ergodic theory lecture notes](https://terrytao.wordpress.com/category/teaching/254a-ergodic-theory/). Verify the exact theorem hypotheses when applying pointwise or mean convergence results.
