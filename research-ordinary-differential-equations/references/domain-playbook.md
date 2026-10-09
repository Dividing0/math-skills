# Existence, uniqueness and continuation

## Choose a branch
- Local initial-value problem: continuity of f(t,y) supports local existence in finite dimension; local Lipschitz continuity in y supports uniqueness. State the open domain and initial point; continuity alone does not give uniqueness.
- Continuation: a local solution extends while it stays in a compact subset of the vector field's domain over a bounded time interval. Prove an a priori bound or an invariant region before declaring global existence; a global Lipschitz condition in y is a useful sufficient condition with suitable time regularity.
- Stability or numerics: linearize at equilibria but check eigenvalues and nonlinear hypotheses. Eigenvalues with zero real part are inconclusive for linearization. Stiff numerical integration, local truncation estimates and analytic stability address different questions.

## Worked bounded solution
For y'=1-y, y(0)=3, multiply by e^t to obtain (e^t y)'=e^t. Integration gives y(t)=1+2e^(-t). Direct differentiation verifies the equation and initial value. On t>=0 the solution lies in [1,3], converges to the equilibrium 1, and is defined for every finite time. The globally Lipschitz vector field with constant one establishes uniqueness independently of solving the formula. Its derivative -1 at the equilibrium matches asymptotic stability.

## Tempting inference and counterexample
A continuous right-hand side need not give uniqueness. On y>=0, y'=2sqrt(y), y(0)=0 admits y=0 and, for each a>=0, y(t)=0 for t<=a and y(t)=(t-a)² for t>=a. Both pieces join differentiably and satisfy the equation at a. Local Lipschitz continuity in y fails at zero; a solver choosing the zero path does not prove other paths impossible.

## Stop or hand off
When a solution approaches a domain boundary, distinguish a coordinate singularity, true blow-up and loss of the specified equation's validity. Pass the maximal interval, events and invariant region to numerical work. State whether tolerances control local error estimates or certified global error. Do not infer uniqueness or global continuation solely from an apparently smooth computed trajectory.
