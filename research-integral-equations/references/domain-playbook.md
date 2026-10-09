# Solvability versus stable inversion

## Choose a branch
- Contraction for second kind: for u=f+lambda Ku on a Banach space, verify K bounded and |lambda|*norm(K)<1. The Neumann series then supplies a unique solution and a geometric truncation bound; a kernel formula by itself does not verify the norm.
- Fredholm route: for compact K on a Hilbert space, I-lambda K is Fredholm of index zero. At a noninvertible value, solvability requires f orthogonal to the adjoint nullspace. State the inner product, lambda convention and kernel space.
- First-kind regularization: for Ku=f, inspect range closure and singular values. If singular values approach zero, inverse amplification may be unbounded. A regularized solution depends on noise scale and parameter choice, not only on the equation residual.

## Worked rank-one equation
On C[0,1] with the sup norm, let Ku(x)=integral_0^1 u(t)dt. This is a constant function and norm(K)=1. For u(x)=x+(1/2)Ku(x), set c=integral u. Integrating gives c=1/2+c/2, hence c=1, and u(x)=x+1/2. Direct substitution verifies the equation. The contraction constant is 1/2, so uniqueness holds throughout this space rather than only within an ansatz of affine functions.

## Tempting inference and counterexample
A small residual is not small solution error in an ill-conditioned first-kind problem. On l² define K e_n=e_n/n. For approximate u_n=e_n and exact solution zero to f=0, the residual norm is 1/n→0 while solution error remains one. K is injective and compact but its inverse on its range is unbounded. Report both the norm and conditioning assumptions before interpreting residuals.

## Stop or hand off
If a singular kernel needs a principal value, specify and justify that interpretation before exchanging integrals. When Fredholm compatibility is unknown, return the adjoint nullspace obligation. Pass measured noise, function spaces and spectral information to inverse-problem regularization. Numerical quadrature error, regularization bias and data noise are distinct terms; give a bound only for those actually controlled.
