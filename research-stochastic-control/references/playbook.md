# Research Stochastic Control: playbook

## Exact finite-horizon recursion

For stage cost c and discount gamma, set V_T to the terminal cost and compute `V_t(s)=min_a[c(s,a)+gamma*sum(P(s_next|s,a)*V_{t+1}(s_next))]`. The helper uses exact rational arithmetic and chooses the lowest action index on ties. Its policy is time-dependent; replacing it by one stationary row changes the problem.

For a single state with one action, cost 2, terminal cost 3, horizon 2 and gamma=1/2, values are V_2=3, V_1=7/2 and V_0=15/4. This checks discount placement, terminal handling and backward order independently.

In a partially observed model, the observation alone need not be a sufficient Markov state. A belief-state formulation or another justified information state is required before applying a fully observed Bellman recursion. Continuous-time verification additionally requires admissibility, regularity and appropriate terminal/transversality conditions.

## Acceptance cases

- Horizon zero: return terminal values and no actions.
- Finite horizon with discount one: valid here; do not import an infinite-horizon contraction claim.
- Transition rows do not sum to one: reject the model rather than normalize silently.
- Controller observes future noise: reject the claimed admissible policy.
- A discretized HJB residual is small: report numerical evidence, not a verification theorem.

## Primary sources

[Dimitri Bertsekas, Dynamic Programming and Optimal Control materials](https://web.mit.edu/dimitrib/www/dpchapter.html).
