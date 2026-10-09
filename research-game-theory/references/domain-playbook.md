# Equilibrium under a stated deviation model

## Method branches
1. For a finite normal-form game, enumerate pure best responses and check every unilateral deviation. Mixed strategies are probability distributions over actions; expected payoffs are computed using independent randomization unless a correlation device is specified.
2. For a two-player zero-sum game, normalize one player's payoff matrix and use the opposing sign for the other. Linear-program or minimax certificates need primal and dual feasibility. Their value guarantees are specific to zero-sum structure.
3. For a mixed equilibrium with small supports, solve indifference equations among supported actions, then check that unsupported actions cannot improve the payoff. Indifference alone does not ensure probabilities lie in the simplex or that every deviation is blocked.
4. For sequential games, use backward induction when the game has finite horizon and perfect information. For imperfect information, specify information sets and beliefs; normal-form Nash equilibrium need not rule out incredible off-path threats.

5. For a correlated equilibrium, specify a joint distribution p(a)≥0 with total mass one. For each player i and recommendation a_i versus deviation b_i, check Σ_(a_-i) p(a_i,a_-i)[u_i(a_i,a_-i)-u_i(b_i,a_-i)]≥0. These unnormalized obedience inequalities cover zero-probability recommendations without division. Correlation replaces independent randomization; Nash support indifference equations alone do not certify this concept.

## Worked calculation
Consider two players choosing H or T, with row payoff +1 on matching actions and -1 otherwise, and column payoff its negative. If column chooses H with probability q, row's H payoff is 2q-1 and T payoff is 1-2q. Indifference gives q=1/2. The symmetric column calculation gives row probability p=1/2. Against these strategies each pure deviation earns zero, so mixtures cannot improve either player's payoff. The equilibrium value is zero.

## Tempting inference and counterexample
A Nash equilibrium need not maximize total welfare. In a prisoner's dilemma, assign payoffs (3,3) to mutual cooperation, (1,1) to mutual defection and (5,0)/(0,5) to unilateral defection. Defection strictly dominates cooperation, yielding equilibrium (1,1), although mutual cooperation has total payoff six rather than two.

## Stop and handoff
Stop an equilibrium calculation if payoff signs, information or permissible deviations are unspecified. Pass payoff tables, action supports, probability vectors, deviation inequalities and equilibrium concept to verification. Separate predictions about rational play from normative welfare claims. For approximate equilibria state a maximum deviation gain and the units of payoffs; solver termination alone is not an incentive certificate.
