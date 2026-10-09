# From brackets to local and global groups

## Method branches
1. For a matrix Lie algebra over R or C, compute [A,B]=AB-BA and verify the proposed subspace is closed. Antisymmetry and Jacobi follow from the commutator in an associative algebra, but closure still requires checking for the particular subspace.
2. For a matrix Lie group, differentiate the defining relations at the identity to obtain necessary tangent conditions. Show candidate tangent vectors arise from curves or exponentials before claiming equality of the tangent space.
3. For exponential-map arguments in finite-dimensional real Lie groups, use local invertibility near zero. Global surjectivity, injectivity or a logarithm branch needs separate group-specific hypotheses.
4. For integrating Lie-algebra morphisms, use the connected simply connected source-group setting when applying the standard integration theorem. Quotients by discrete central subgroups can share a Lie algebra but have different global topology and representations.

## Worked calculation
For SO(2), differentiate A(t)ᵀA(t)=I at A(0)=I to obtain Xᵀ+X=0. Every such 2-by-2 matrix is θJ with J=[[0,-1],[1,0]]. Since J²=-I, the exponential series gives exp(θJ)=cos θ I+sin θ J, which is in SO(2). Thus the tangent condition is realized, and periodicity exp((θ+2π)J)=exp(θJ) also displays failure of global injectivity.

## Tempting inference and counterexample
Every real invertible matrix is not the exponential of a real matrix. For any real B, det exp(B)=exp(trace B)>0. The one-by-one matrix [-1] has negative determinant and is invertible, but cannot equal exp(B) for real B. A local exponential theorem cannot remove this global obstruction.

## Stop and handoff
Stop a classification or integration claim when connectedness, simple connectedness, characteristic or topology is unspecified. Pass bracket conventions, exact tangent equations, exponential domain and kernel information to representation or geometry work. Distinguish the universal covering group from a chosen quotient, especially when deciding which infinitesimal representations descend globally.
