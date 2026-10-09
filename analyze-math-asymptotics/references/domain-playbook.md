# Asymptotic regimes and remainder control

## Choose a branch
- Taylor expansion: fix a center and a neighborhood on which the required derivative is bounded. For a degree m expansion, a bound on derivative m+1 supplies a remainder of order m+1. A constant depending on an auxiliary parameter does not establish uniformity in that parameter.
- Dominant balance: rescale every term using the proposed parameter powers, retain tied leading orders, and check that discarded terms really vanish on the proposed solution scale. Repeat near points where a leading coefficient vanishes.
- Laplace integrals: for a compact integration interval, a unique interior nondegenerate minimum of a smooth phase and a continuous amplitude permit the standard Gaussian leading term. Boundary minima, several minima and vanishing curvature require different local models; first prove a positive phase gap outside the minimum neighborhood.

## Worked calculation
For x tending to zero, consider g(x)=sqrt(1+x). On |x|<=1/2, g^(3)(x)=3/[8(1+x)^(5/2)], whose magnitude is at most 3*2^(5/2)/8. Taylor's formula therefore gives g(x)=1+x/2-x²/8+R(x), with |R(x)|<=2^(5/2)|x|³/16. This is a uniform numerical constant on the stated interval, rather than an unspecified formal term. The estimate controls truncation, not the rounding of an implementation.

## Tempting inference and counterexample
Pointwise smallness does not imply uniform smallness over a moving domain. For h_e(x)=e*x, each fixed real x has h_e(x)→0 as e→0, but sup over 0<=x<=1/e is 1. A fixed-x expansion cannot silently be used at x=1/e. Report which coupled limit is requested before choosing terms.

## Stop or hand off
If the phase has an unresolved degenerate stationary point, preserve the exact integral and send its local scaling problem to perturbation analysis. If a remainder estimate needs an unproved derivative bound, label the expansion formal. Deliver parameter ranges, direction of limits, constants, and the strongest established error statement to numerical work. Numerical agreement supports diagnostics but does not discharge a uniform remainder obligation.
