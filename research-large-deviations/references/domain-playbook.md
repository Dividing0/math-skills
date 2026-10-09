# Domain playbook: research-large-deviations

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For independent identically distributed variables with log moment-generating function finite in a neighborhood of zero, Cramér's theorem gives a sample-mean LDP with speed n and Legendre-transform rate. For a finite-state empirical distribution, Sanov-type arguments use relative entropy and the specified probability simplex topology. For continuous maps, contraction transfers an established LDP with rate infimum over preimages; it does not justify discontinuous transformations automatically. For any claimed full LDP, verify lower bounds on open sets and upper bounds on closed sets, and distinguish exponential tightness from ordinary tightness.

## Worked valid example

For iid Bernoulli(1/2) variables, the event that their sample mean equals one is exactly the event that all n bits equal one. Its probability is 2^-n, hence (1/n)log P=-log 2. The Bernoulli relative-entropy candidate rate at one is 1·log(1/(1/2))+0·log(0/(1/2))=log 2, using 0 log 0=0. This endpoint event permits an exact calculation as well as an asymptotic consistency check; it does not derive all LDP bounds.

## Tempting invalid inference

An asymptotic rate omits polynomial prefactors. For even n and fair bits, P(mean=1/2)=binom(n,n/2)2^-n decreases like a constant times n^-1/2, while its logarithmic rate is zero. exp(-n·0)=1 is not the finite-n probability.

## Stop and handoff

Return the random family, topology, speed and rate with the theorem hypotheses checked. If moment-generating functions fail near zero, stop the Cramér shortcut and inspect heavy-tail alternatives. Transfer finite-sample guarantees to concentration bounds rather than presenting rates as exact probabilities.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
