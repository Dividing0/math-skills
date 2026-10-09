# Domain playbook: analyze-model-identifiability

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For a finite noiseless observation map F:Θ→R^m, first solve F(θ)=F(θ₀) on the entire admissible domain; uniqueness is a global statement. For maps C¹ on an open neighborhood of an interior parameter point, a full-column-rank Jacobian there gives local injectivity after selecting an invertible square minor and applying the inverse function theorem, but not global injectivity. For noisy observations, use the specified error covariance and scaled sensitivities to assess information; profile likelihood or uncertainty regions require the actual observation/error model and are not structural proofs.

## Worked valid example

Let y(t)=a+bt with a,b real and exact samples y(0)=2,y(3)=8. The observation matrix is [[1,0],[1,3]], whose determinant is 3. Subtracting the observations gives 3b=6, so b=2 and a=2. This calculation proves global uniqueness on R², not merely a well-behaved optimizer. If only y(0) were observed, every pair (2,b) would agree.

## Tempting invalid inference

Full derivative rank everywhere need not establish global identifiability: F(θ)=θ² on R\{0} has derivative 2θ≠0, yet F(2)=F(-2). Restricting the domain to θ>0 repairs this particular ambiguity; it must be an application assumption rather than an arbitrary estimation convenience.

## Stop and handoff

Hand off the observation map, admissible parameter set, explicit equivalent parameter pairs and feasible intervention constraints to measurement selection. Stop short of precision claims when noise or sample design is unspecified.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
