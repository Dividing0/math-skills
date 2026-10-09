# Domain playbook

## Select the method

1. For elliptic Dirichlet problems, formulate the bilinear form on H0^1 and check boundedness, coercivity and the load's dual-space membership. Existence of a weak solution does not automatically establish classical second derivatives.
2. For evolution equations, derive an energy identity with the actual boundary terms and regularity. Use estimates for uniqueness and continuous dependence; establish existence independently through a justified construction.
3. For first-order transport, characteristics require the corresponding coefficient regularity and compatible inflow or initial data. When characteristics intersect or singularities develop, specify a weak solution and any selection criterion rather than continuing a classical formula without justification.

## Worked check

For u_t=u_xx on (0,1) with zero boundary values and a sufficiently smooth solution, multiplying by u and integrating yields (1/2)d/dt integral u²=-integral (u_x)²; the boundary term uu_x vanishes. Applying the same identity to the difference of two solutions with equal initial data gives nonincreasing nonnegative energy initially zero, hence uniqueness in the justified class.

## Invalid inference and witness

A spatially smooth forcing need not make inconsistent initial and boundary data classical at the corner. Asking u_t=u_xx, u(0,t)=0 for t>=0, and u(x,0)=1 on [0,1] imposes both u(0,0)=0 and 1. A weaker formulation may be possible, but no continuous solution satisfies all those pointwise conditions.

## Completion and handoff

Return domain, coefficients, initial/boundary conditions, compatibility, function spaces and solution notion. Stop at unsupported regularity or uniqueness claims. Hand numerical PDE work the analytic target and conserved quantities; hand Sobolev-space analysis the trace and embedding obligations, keeping weak existence separate from classical solvability.
