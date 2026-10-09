# Domain playbook: certify-math-computations

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For rational polynomial identities or finite combinatorial claims, prefer exact arithmetic and a checkable witness; enumerate every admissible case only after proving the domain finite and correctly represented. For scalar root existence, use a continuous function on a closed interval and exact or outward-rounded opposite endpoint signs. For uniqueness, add a derivative enclosure excluding zero on the same interval. For interval Newton or multidimensional certificates, verify the particular inclusion theorem, nonsingular preconditioner and outward rounding at every operation instead of transferring a scalar sign argument.

## Worked valid example

For f(x)=x²-2 on [7/5,3/2], exact rational evaluation gives f(7/5)=-1/25 and f(3/2)=1/4. Continuity yields a root. The derivative 2x lies in [14/5,3], hence f is strictly increasing and there is exactly one root in this interval. This certifies one positive root, not completeness over R: a negative root also exists. Endpoint signs, domain and derivative bound form a small independently checkable certificate.

## Tempting invalid inference

A tiny residual need not imply a nearby root: f(x)=10^-20(1+x²) has residual 10^-20 at zero and no real root. Increasing floating-point precision cannot change this mathematical obstruction.

## Stop and handoff

Return exact input interpretation, enclosures, coverage region and checker dependencies. If a transcendental interval library lacks documented directed rounding, report an unverified numerical enclosure and transfer implementation obligations to numerical auditing.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
