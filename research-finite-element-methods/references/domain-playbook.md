# Domain playbook

## Select the method

1. For conforming Galerkin approximation, specify a Hilbert space V, a bounded coercive bilinear form a, bounded load functional and subspace V_h subset V. Galerkin orthogonality then supports an error bound by the best approximation, with explicit continuity/coercivity constants.
2. For mixed formulations, identify both trial spaces, nullspaces and the discrete inf-sup constant. Mesh-independent stability must be checked for the chosen pair; element labels alone do not establish it.
3. For nonconforming or quadrature-based methods, add consistency and quadrature terms rather than applying the conforming estimate unchanged. State mesh shape regularity and solution regularity before predicting approximation order.

## Worked check

For -u''=1 on (0,1), zero endpoint values, use continuous piecewise linears with a single interior node at 1/2. Its hat φ has derivative ±2, so a(φ,φ)=4 and load integral φ=1/2. Writing u_h=cφ yields 4c=1/2, hence c=1/8. The exact u=x(1-x)/2 agrees at the node, but differs between nodes.

## Invalid inference and witness

Exact nodal agreement does not imply exact finite-element solution. At x=1/4, the previous u_h equals 1/16 while u equals 3/32. A zero nodal error can hide nonzero energy and interior errors. Report the norm being tested and a function-level comparison.

## Completion and handoff

Return weak form, boundary treatment, spaces, matrix assembly, stability constant and all error components. Stop if discrete coercivity or inf-sup is unsupported. Hand numerical implementation basis functions, quadrature, constraints and norm definitions; hand proof review the interpolation and stability estimates needed for the claimed rate.

Before reporting success, recheck the selected branch against the exact requested conclusion. Record which premises came from the user and which were derived. A missing premise must remain an explicit obligation, with a concrete description of the additional input or proof needed to continue.
