# Algorithm selection and stopping evidence

## Choose a branch
- Smooth convex descent: for a differentiable convex function with an L-Lipschitz gradient, a fixed step no larger than 1/L supplies a standard descent estimate. To claim a linear rate, add strong convexity and state its parameter. A numerically guessed L is not a verified global bound.
- Newton or quasi-Newton: check derivative formulas and linear-solve accuracy. Local fast convergence needs a nonsingular appropriate Hessian and neighborhood assumptions; globalization requires a line search or trust region with stated conditions.
- Constrained or nonsmooth optimization: choose projected or proximal steps when the projection/proximal operator is well defined. For smooth convex constrained work on a closed convex set, use a projected-gradient mapping as a stationarity residual; also report constraint violation.

## Worked quadratic iteration
Let f(x,y)=(x²+4y²)/2. Its gradient is (x,4y), Hessian diag(1,4), and L=4 with strong-convexity constant 1 in Euclidean norm. Gradient descent with step 1/4 updates x_next=3x/4 and y_next=0. From (2,1), one step gives (3/2,0), then x decays geometrically. The objective can be calculated exactly at every step, and the gradient norm independently checks stationarity. This derivation exposes the condition number 4 and the chosen scale rather than trusting a generic optimizer status flag.

## Tempting inference and counterexample
Tiny motion does not mean small error. For f(x)=x²/2 at x=1, a step size 10^(-12) gives displacement 10^(-12) while gradient remains approximately 1 and the minimizer is zero. A displacement-only stopping rule reports success solely because the step was chosen tiny. Likewise stationarity without convexity does not prove global optimality: f(x)=-x² is stationary at zero, a strict maximum.

## Stop or hand off
If an oracle's gradient noise is unknown, report a residual for the supplied oracle, not exact stationarity. Pass conditioning, smoothness constants, feasibility tolerances and derivative checks to implementation. Record objective progress, scaled stationarity and feasibility separately. A failed line search, iteration cap or singular solve is a computational outcome; state it honestly and preserve the last iterate rather than fabricating convergence.
