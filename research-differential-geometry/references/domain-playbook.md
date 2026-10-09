# Domain playbook

## Select the method

1. For coordinate computations, fix charts and tensor conventions. Verify transformation laws before treating arrays as geometric objects; ordinary second partial derivatives are not automatically tensor components.
2. For Riemannian geodesics, derive the connection from the metric and solve the geodesic equation on its chart interval. Global extension requires an independent completeness argument, not merely smooth local coefficients.
3. For embedded hypersurfaces, specify the normal and curvature-sign convention. Compute induced metric and second fundamental form, then distinguish intrinsic curvature from embedding-dependent principal curvatures.

## Worked check

On the Euclidean plane in polar coordinates away from r=0, g=diag(1,r²). The connection formula gives Γ^r_{θθ}=-r and Γ^θ_{rθ}=Γ^θ_{θr}=1/r. Thus geodesics satisfy r''-r(θ')²=0 and θ''+2r'θ'/r=0. Nonzero Christoffel symbols coexist with zero intrinsic curvature because polar coordinates are non-Cartesian.

## Invalid inference and witness

A chart representation cannot justify global injectivity. The smooth map t->(cos t,sin t) from R to the circle has nonzero derivative everywhere and is locally regular, but t and t+2π have the same image. Local immersion data does not establish a global embedding or a single global coordinate.

## Completion and handoff

Return chart domains, regularity, metric or connection, orientation and curvature conventions. Stop at coordinate singularities until another chart or an intrinsic argument is available. Hand topology global obstruction questions and ODE analysis the actual geodesic initial-value problem; separate a local solution from a complete geodesic.

Before reporting success, recheck the selected branch against the exact requested conclusion. Record which premises came from the user and which were derived. A missing premise must remain an explicit obligation, with a concrete description of the additional input or proof needed to continue.
