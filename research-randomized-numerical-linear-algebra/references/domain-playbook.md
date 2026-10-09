# Domain playbook

## Select the method

1. For a range finder, form Y=AΩ and an orthonormal basis Q. The deterministic residual is ||(I-QQ*)A|| in a specified norm; probabilities concern the sketch distribution and must be stated separately from this identity.
2. For Gaussian sampling, fix target rank, oversampling and independence. Use a precise theorem when converting these parameters to an expectation or failure bound; a successful seed is not a bound for all sketches.
3. For least-squares sketching, verify a subspace-embedding property on the column space of [A,b] or the appropriate theorem's space. For leverage sampling, specify leverage estimates, probabilities, rescaling and sample count; uniform sampling can fail for highly concentrated leverage.

## Worked check

Take A=diag(3,0) and Ω=(1,2)^T. Then Y=(3,0)^T and Q=(1,0)^T. Thus QQ^T A=A and the range-approximation residual is exactly zero. This is a deterministic check for a rank-one matrix and a nonzero sampled component, not a probability guarantee for other matrices or sketches.

## Invalid inference and witness

One sampled column can miss the entire range. For the same A and Ω=(0,1)^T, Y=0 and its span captures none of A; the spectral residual is three. A Gaussian sketch makes this exact event probability zero, but a coordinate-sampling sketch may assign it positive probability. Distribution is mathematically decisive.

## Completion and handoff

Return access model, matrix dimensions, target rank, norm, distribution, failure probability and arithmetic errors. Stop before assigning a confidence level without an applicable bound. For further bounds consult Halko, Martinsson and Tropp, Finding Structure with Randomness, SIAM Review 53 (2011), §4.1 and later error analysis, https://arxiv.org/abs/0909.4061; verify exact assumptions before quoting a theorem. Hand implementation reproducible seeds plus independent residual checks.
