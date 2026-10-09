# Domain playbook: research-computational-geometry

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For orientation or incidence predicates with integer/rational inputs, compute determinant signs exactly; bit complexity depends on input bit length. For floating coordinates, a filtered predicate may use a certified rounding-error bound and fall back to exact arithmetic when uncertain. For convex hull algorithms, decide whether boundary collinear points are retained, then use consistent turn and duplicate policies. For arrangements or intersections, define overlapping segments and endpoint contacts separately; general-position sweep invariants must be adapted before accepting degenerate input.

## Worked valid example

For A=(0,0), B=(3,1), C=(2,2), orientation is det(B-A,C-A)=3·2-1·2=4>0, so C lies left of directed AB. For D=(6,2), the determinant is 3·2-1·6=0, so A,B,D are collinear; the dot-product or coordinate bounds further show D is beyond segment AB. Zero orientation alone therefore does not imply segment membership. These integer computations need no tolerance policy.

## Tempting invalid inference

Independent rounding of coordinates can reverse a nearly degenerate orientation. For A=(0,0),B=(1,1),C=(2,2+ε), the exact determinant is ε; if 2+ε rounds to 2, a floating calculation reports zero. An arbitrary epsilon threshold conflates geometric uncertainty with arithmetic error.

## Stop and handoff

Specify input interpretation, degeneracy conventions and output encoding. If exact input cannot be recovered from uncertain measurements, return an uncertainty classification rather than an exact topological claim. Pass large-bit arithmetic requirements to implementation and certificate checking.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
