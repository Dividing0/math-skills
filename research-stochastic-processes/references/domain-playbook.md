# Domain playbook: research-stochastic-processes

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For a finite-state Markov chain, specify row/column transition convention and solve stationarity with normalization; convergence from all initial laws additionally needs the relevant irreducibility/aperiodicity conditions. For discrete-time martingales, verify adaptation, integrability and conditional-expectation identity against the stated filtration. For optional stopping, bounded stopping times allow a standard integrable-martingale argument; unbounded times need uniform integrability or another precise theorem. For Brownian stochastic integration, use adapted predictable integrands with the required square-integrability for an L² Itô integral, and name the integral convention.

## Worked valid example

Take a two-state chain with row transition matrix P=[[3/4,1/4],[1/2,1/2]]. Write its stationary law as (p,1-p). The first-coordinate equation is p=(3/4)p+(1/2)(1-p), giving (3/4)p=1/2 and p=2/3. Hence π=(2/3,1/3). Positive transition probabilities imply irreducibility and aperiodicity. A direct recurrence p_{n+1}=1/2+p_n/4 yields p_n-2/3=(1/4)^n(p₀-2/3), proving convergence without conflating stationarity and transient laws.

## Tempting invalid inference

Stationarity does not imply independent states: X_n=Z for all n with nondegenerate Bernoulli Z is stationary but its states coincide. Its zero increments are independent, so it is not an increments counterexample. For dependent increments instead let X_n=(-1)^n Z, with P(Z=1)=P(Z=-1)=1/2. Its joint laws are shift-invariant, while successive increments -2Z and 2Z are perfectly dependent. Nor does a unique stationary law alone remove periodic oscillations in a Markov chain.

## Stop and handoff

Return filtration, dependence assumptions and exact theorem conditions. If a stopping-time argument lacks an integrability condition, preserve the unresolved expectation interchange. Transfer simulation estimates to computational experiments and diffusion existence assumptions to stochastic/PDE analysis.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
