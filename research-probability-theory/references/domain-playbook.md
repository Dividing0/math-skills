# Dependence, convergence and conditioning kept distinct

## Method branches
1. For moment identities, first check integrability. Independence permits factorization of expectations when the relevant products are integrable. Zero covariance alone is weaker than independence and says nothing about nonlinear dependence.
2. For convergence questions, name almost sure, in-probability, Lᵖ or distributional convergence. Convergence in probability plus uniform integrability can justify convergence of first moments; probability convergence alone cannot.
3. For conditional probabilities, define the conditioning sigma-algebra and identify null-set ambiguity. Conditional expectation is specified only almost surely; conditioning on a probability-zero event requires a regular conditional or limiting construction with its interpretation stated.
4. For finite Markov chains, distinguish stochasticity, irreducibility and aperiodicity. Irreducibility supplies uniqueness of a stationary distribution in the finite setting, while aperiodicity controls convergence of powers. A stationary equation is not itself a mixing proof.

## Worked calculation
Let X be uniform on {-1,0,1} and Y=X². E[X]=0, E[Y]=2/3 and E[XY]=E[X³]=0, so Cov(X,Y)=0. Yet X and Y are dependent: P(Y=0|X=0)=1 differs from P(Y=0)=1/3. This finite calculation makes the distinction explicit without relying on simulation.

## Tempting inference and counterexample
Let U be uniform on (0,1) and Xₙ=n·1{U≤1/n}. Then P(|Xₙ|>ε)=1/n for n>ε, so Xₙ→0 in probability, but E[Xₙ]=1 for every n. Interchanging expectation and the probability limit is unjustified without additional control of tails or domination.

## Stop and handoff
Stop a limit-theorem application when dependence, moments or the convergence mode is unspecified. Pass the probability space, sigma-algebras, dependence assumptions, tail bounds and precise mode of convergence to stochastic-process or statistics work. State whether a claim concerns a stationary law or convergence toward it, and whether a numerical experiment checked only finite n rather than establishing an asymptotic theorem.
