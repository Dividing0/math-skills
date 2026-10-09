# Domain playbook: research-real-analysis

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For uniform convergence on a fixed set, compute or bound a supremum independent of the point; continuity passes to the limit when the approximants are continuous. For exchanging integration and limits, choose dominated convergence with an integrable dominator, monotone convergence for increasing nonnegative functions, or another theorem with its own hypotheses. For derivatives on a compact interval, uniform convergence of continuous derivatives plus convergence at one base point yields a differentiable limit via the fundamental theorem of calculus. For compactness arguments, establish closedness and boundedness in finite-dimensional Euclidean space; infinite-dimensional analogues require separate criteria.

## Worked valid example

On [0,1], f_n(x)=x+x²/n converges uniformly to f(x)=x because sup|f_n-f|=1/n. Its derivatives are 1+2x/n and converge uniformly to one with supremum error 2/n. Also f_n(0)=0. Integrating the derivative identity from zero gives f_n(x)=∫₀ˣ(1+2t/n)dt; uniform convergence permits the integral limit, yielding f(x)=∫₀ˣ1dt=x and f'=1. Both function and derivative claims have explicit estimates.

## Tempting invalid inference

Pointwise convergence does not guarantee convergence of integrals. On (0,1), f_n(x)=n·1_(0,1/n)(x) tends to zero at every fixed x>0, yet every integral equals one. No single integrable dominator can support the proposed dominated-convergence application.

## Stop and handoff

Return the precise convergence mode, domain and endpoint treatment. When a supremum or dominator cannot be justified, avoid exchanging operations and search for concentration near moving boundaries. Transfer measure-theoretic subtleties to measure theory with the same functions and measure.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
