# Domain playbook: select-identifying-measurements

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For linear observations y=Aθ, structural identification of all finite-dimensional unknowns requires full column rank; choose extra rows that remove the actual nullspace. For nonlinear observations, local Jacobian rank can guide design at an interior nominal parameter, but global distinguishability requires checking equality of full observation vectors on the admissible domain. For noisy measurements, whiten sensitivities using a justified covariance matrix and compare information objectives only after fixing parameter scales and cost. For interventions, verify that they are feasible and change the observation map rather than merely repeat identical information.

## Worked valid example

Suppose θ=(a,b) and the existing exact measurement is y₁=a+b. Its nullspace is span((1,-1)), so additional copies of y₁ cannot distinguish those changes. A proposed sensor y₂=a-b yields matrix [[1,1],[1,-1]] with determinant -2. The two readings recover a=(y₁+y₂)/2 and b=(y₁-y₂)/2 globally. In contrast y₂=2(a+b) has dependent rows and leaves the nullspace unchanged. This explicitly compares structural designs before considering noise reduction.

## Tempting invalid inference

Replicating y=θ² can improve precision about θ² but never distinguish θ from -θ on R. A signed measurement y₂=θ resolves the ambiguity; a domain restriction θ>0 also changes the identification problem and must be independently justified.

## Stop and handoff

Return proposed sensors, costs, removed symmetries and remaining ambiguities. If feasible interventions or noise covariance are unknown, present structural alternatives and mark efficiency comparisons conditional. Hand the exact updated map to identifiability analysis before expensive data collection.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
