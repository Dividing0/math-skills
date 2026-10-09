# Operators with domains before formal manipulations

## Method branches
1. For an unbounded operator on a Hilbert space, supply a dense domain and define its adjoint by the inner-product identity. Symmetry means inclusion in the adjoint; self-adjointness requires equality of operators and domains. Boundary terms often decide the distinction.
2. For spectral expansions, state the applicable spectral theorem and whether the spectrum is discrete or continuous. An orthonormal eigenbasis needs more than a formal eigenvalue equation; compact resolvent is one common route for a self-adjoint operator.
3. For conservation laws, compute commutators only on a domain where both compositions exist. Extending a formal identity to a dynamical conservation statement requires a well-defined evolution and domain control.
4. For approximations, specify a small parameter, scale and topology of convergence. Dimensional analysis checks consistency but does not bound truncation error or establish operator convergence.

## Worked calculation
For the Dirichlet Laplacian A=-d²/dx² on (0,π), take domain H²(0,π)∩H₀¹(0,π) in L². Functions sin(nx), n≥1, satisfy the boundary conditions and A sin(nx)=n² sin(nx). Integration by parts gives ⟨Au,u⟩=∫|u′|²≥0 for that domain. This proves positivity for these admissible functions; completeness of the sine system is a separate Fourier theorem, not a consequence of solving the differential equation alone.

## Tempting inference and counterexample
A differential expression alone does not determine its spectrum. For -u″ on (0,π), Neumann boundaries admit the constant eigenfunction with eigenvalue zero. Dirichlet boundaries exclude it and the smallest eigenvalue is one. Ignoring the domain conflates two different operators.

## Stop and handoff
Stop before labeling an operator self-adjoint when only integration by parts on compactly supported test functions has been checked. Pass the Hilbert space, operator domain, boundary conditions, sign/inner-product conventions and unresolved extension questions to functional analysis. Label a formal mode expansion as formal until completeness and its convergence sense are justified. Keep physical units and mathematical normalization visible when comparing energies or frequencies.
