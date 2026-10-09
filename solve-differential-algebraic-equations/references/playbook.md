# Solve Differential-Algebraic Equations: playbook

## Linear index-one example

The helper solves `x_prime=A x+B z+f`, `0=C x+D z+g`, with constant coefficients and invertible D. Eliminate `z=-D^{-1}(Cx+g)` using linear solves. The example gives `z=-x` and `x_prime=-2x`, so `x(t)=exp(-2t)` for x(0)=1. Backward Euler at h and h/2 is compared to an augmented-matrix exponential reference.

An algebraic initial value other than -1 in that example is inconsistent. Reject it rather than silently modifying a user-specified initial state. A singular D may still define a meaningful DAE, but it falls outside this elimination helper.

## Acceptance cases

- Singular D: reject the helper request and analyze the index/constraints separately.
- Algebraic initial value disagrees with the constraint: identify the inconsistency.
- Algebraic residual is tiny but time error is large: retain both diagnostics.
- A differentiated constraint is solved without its initial constraint: flag the spurious solution family.
- General nonlinear DAE: use an appropriate residual solver such as IDA, with verified initialization and supported index assumptions.

## Primary sources

[SUNDIALS IDA mathematical considerations](https://sundials.readthedocs.io/en/latest/ida/Mathematics_link.html).
