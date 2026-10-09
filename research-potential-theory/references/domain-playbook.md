# Domain playbook: research-potential-theory

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For classical harmonic functions on a bounded connected domain, use maximum principles with continuity on the closure when comparing boundary values; uniqueness follows by applying the argument to a difference. For weak solutions, specify Sobolev spaces, trace data and the elliptic operator's coercivity instead of assuming classical boundary values exist. For Green representations, verify kernel normalization, singularities and boundary conditions before integration by parts. For unbounded domains, add and verify behavior at infinity; bounded-domain compactness cannot be silently transferred.

## Worked valid example

On the unit disk, u(x,y)=x²-y² is harmonic because u_xx+u_yy=2-2=0. On the boundary x=cos θ,y=sin θ, its values are cos(2θ). Thus u supplies a classical solution to that Dirichlet problem. If v is another harmonic solution continuous on the closed disk with identical boundary data, w=u-v has boundary zero. The maximum principle gives w≤0 and applying it to -w gives w≥0; hence v=u.

## Tempting invalid inference

The function log(r) is harmonic for r>0 in the plane but has a singularity at r=0. Treating it as harmonic on the full disk and applying bounded-domain maximum principles is invalid. The punctured domain or a distributional source at zero changes the problem.

## Stop and handoff

Return operator sign convention, domain regularity, solution notion and boundary/decay assumptions. Missing trace or growth data must be listed as unresolved. Transfer weak existence arguments to PDE/functional analysis and numerical boundary approximations to numerical PDE.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
