# Domain playbook: research-spectral-graph-theory

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For a finite undirected graph with nonnegative symmetric weights, use L=D-A and the quadratic form xᵀLx=Σ_{unordered edges}w_ij(x_i-x_j)². Connectivity depends on the support of positive weights.
- For normalized Laplacians, state how zero-degree vertices are handled before importing eigenvalue ranges or zero-multiplicity claims. Similarity to a random-walk operator requires an invertible degree matrix on the relevant support.
- For optimization relaxations, specify the orthogonality and normalization constraints in a Rayleigh quotient. Rounding a Fiedler vector creates a discrete cut, whose quality needs a separate analysis.

## Worked valid example

For the unweighted three-vertex path, L=[[1,-1,0],[-1,2,-1],[0,-1,1]]. Vectors (1,1,1), (1,0,-1) and (1,-2,1) have eigenvalues 0,1 and 3 respectively by direct multiplication. The zero eigenspace consists of constants: the quadratic form vanishes only when x₁=x₂=x₃. Thus the path is connected, and its algebraic connectivity is 1 under this unnormalized convention.

## Tempting inference and counterexample

Negative weights destroy the positive quadratic-form argument. A two-vertex edge of weight -1 gives L=[[-1,1],[1,-1]] with eigenvalues 0 and -2. The graph support is connected, but the Laplacian is not positive semidefinite; ordinary nonnegative-weight spectral inequalities do not apply.

## Stop conditions and handoff

Stop a numerical connectivity verdict without exact graph support or an error estimate resolving zero from small positive eigenvalues. Hand off weights, normalization, isolated vertices, spectral residuals and the discrete rounding obligation.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
