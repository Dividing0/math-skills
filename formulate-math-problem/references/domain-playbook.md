# A specification that survives mathematical translation

## Method branches
1. For existence questions, fix objects and quantify the witness after all parameters it may depend on. Separate “for every input there exists a solution” from “there exists one solution valid for every input.” State whether a constructive witness is required.
2. For optimization, define feasible sets, objective direction and parameter dependencies. Ask for a minimum only if attainment is intended; otherwise an infimum and an approximating sequence may be the appropriate output. Include empty-set and unbounded cases.
3. For approximate computation, specify absolute or relative error, norm, confidence if probabilistic, and admissible resource limits. Relative error is undefined at a zero reference unless a mixed tolerance is supplied.
4. For inverse or empirical problems, separate latent objects, observations, noise and modeling assumptions. State which information the agent can observe when choosing an estimator or intervention.

## Worked calculation
“Find the smallest positive number” becomes: find x∈(0,∞) such that x≤y for every y∈(0,∞). No such x exists, since x/2 is positive and smaller. The infimum is nevertheless 0, because 0 is a lower bound and every positive proposed lower bound is exceeded downward by half of itself. Thus requesting a minimum and requesting the infimum produce different valid completion criteria.

## Tempting inference and counterexample
Quantifier order cannot be rearranged casually. For every real a there exists real x with x>a: choose x=a+1. There does not exist one real x larger than every real a: take a=x+1. A proposed formalization that moves x outside the universal quantifier changes the claim.

## Stop and handoff
Stop only when a missing choice changes the deliverable materially, while providing conditional specifications where possible. Hand off the original wording, formal domains, quantifier order, permissible dependence of witnesses, assumptions supplied versus introduced, and acceptance criteria. Include one feasible example and one excluded object so downstream proof or computation can detect unintended interpretations without silently narrowing the original request.
