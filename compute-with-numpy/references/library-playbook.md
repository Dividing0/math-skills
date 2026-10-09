# Dense arrays, shapes and error

Use NumPy for dense finite-dimensional numerical data. Choose SciPy sparse algorithms when materializing an n-by-n dense matrix exceeds the memory budget. Choose exact symbolic or rational tools when the requested conclusion concerns exact algebraic rank or polynomial identities. A float64 calculation cannot silently replace an exact statement.

For Ax=b with square nonsingular A, `numpy.linalg.solve(A,b)` returns the solution approximation. Use `numpy.linalg.cond(A)` or a justified inverse bound to relate residual and forward error. For a singular A, zero residual establishes consistency of an approximation, not unique recovery; state any minimum-norm convention. In current NumPy, vector/matrix right-hand-side shapes matter, so read the API corresponding to the installed version.

Worked example: A=[[3,1],[1,2]], b=[7,5]. Eliminate the second equation to obtain x=(9/5,8/5). The bundled script compares solve against this independently derived vector, computes the infinity-norm residual and checks rejection of a singular system. It also demonstrates that a (2,1) column plus a (2,) vector broadcasts to (2,2). A same-shaped output is not guaranteed just because both arrays contain two values.

A tempting invalid inference is that tiny ||b-Axhat|| implies tiny ||x-xhat||. A=diag(1,10^-12), b=(1,10^-12), xhat=(1,0) has residual 10^-12 but forward error one. A valid claim requires a conditioning or inverse bound, its norm and arithmetic assumptions. Another trap is interpreting a reported numerical rank as exact when singular values lie near the chosen cutoff.

For a downstream task accept an exact problem definition, shapes, dtype/range, norm, tolerance and input uncertainty. Return source, arrays or files, actual versions, RNG configuration, finite-value checks, solver status and residual/oracle checks. Label results approximate_numeric unless another procedure established stronger evidence. Do not infer statistical independence from uncorrelated samples, and do not report empirical randomness as an exhaustive counterexample search.

Primary API sources checked 2026-10-08: solve https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html; broadcasting https://numpy.org/doc/stable/user/basics.broadcasting.html; Generator https://numpy.org/doc/stable/reference/random/generator.html; lstsq https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html. Resolve version-specific defaults during use.
