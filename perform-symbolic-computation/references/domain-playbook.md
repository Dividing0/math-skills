# Domain playbook: perform-symbolic-computation

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For polynomial identities over a stated field, expand or factor with exact coefficients and verify equality algebraically. For solving rational equations, preserve original denominator exclusions through elimination and substitute candidates back. For radicals, logarithms and noninteger powers, specify real or complex branches before transformations; squaring gives only a necessary relation unless signs are retained. For antiderivatives, differentiate the proposed result on each connected domain component and include constants separately where appropriate.

## Worked valid example

Solve sqrt(x+3)=x-1 over R. The original equation requires x+3≥0 and x-1≥0, hence x≥1. Squaring yields x+3=(x-1)², or x²-3x-2=0. Candidates are (3±sqrt(17))/2. The negative candidate violates x≥1; the positive candidate satisfies that inequality and the squared relation, so nonnegative square roots recover the original equation. The solution set has exactly the positive candidate.

## Tempting invalid inference

The logarithm identity log(xy)=log(x)+log(y) requires positive real x,y under the real convention. For complex principal logarithms, x=y=-1 gives log(xy)=0 but log(x)+log(y)=2πi. A formal-looking simplification can therefore change the expression.

## Stop and handoff

Return all parameter exceptions and excluded roots. If branch conventions are absent, provide conditional alternatives rather than guessing. Pass exact expressions, assumptions and singular sets to numerical evaluation; decimal approximations must not silently replace exact coefficients.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
