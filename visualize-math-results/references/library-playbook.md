# A figure whose meaning is inspectable

Choose line plots for ordered trajectories or function samples, scatter plots for observations and phase portraits, and log-log plots only for positive values under a specified empirical power-law comparison. Distinguish a signed residual from its magnitude. A zero error cannot be put on a log axis without an explicit separate representation or bound convention.

The bundled example samples the exact function exp(-2t) at 101 evenly spaced times from zero to two. It renders linear and logarithmic y views with units and an explicit analytic label. On the logarithmic view, log y=-2t is affine; on the linear view, y decays. The script checks both endpoint values analytically, positive log-domain data, PNG signature and nonempty export, and closes the figure. `--self-test` uses a temporary file; `--output /path/figure.png` creates the actual requested artifact.

A tempting wrong inference is that a visually positive sampled curve proves f(x)>0 everywhere. f(x)=(x-1/2)²-10^-6 is positive at many coarse grid points but negative at one-half. Adaptive sampling can reveal trouble but finite pictures do not establish an unrestricted universal statement. Similarly a straight-looking log-log plot on three points does not prove an asymptotic convergence theorem.

For uncertainty plots, declare whether bands are confidence intervals, posterior credible intervals, sample dispersion or validated interval enclosures. Their interpretations differ; drawing similar shaded regions cannot transfer their statistical or rigorous meaning. Preserve data units and comparable axes when contrasting methods; report smoothing and interpolation explicitly.

Accept arrays or an executable generator plus their origin and mathematical target. Return actual exported files, data/generator, labels, units, scale choice, sample grid, checks and unresolved visual or mathematical questions. For runtime comparisons record hardware and conditions through benchmark-python; this skill handles the figure and interpretation rather than fabricating measurements. Numerical results should originate from compute-with-numpy/compute-with-scipy or a specialist adapter, and execution evidence from run-math-python.

Primary APIs checked 2026-10-08: savefig https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html; backends https://matplotlib.org/stable/users/explain/figure/backends.html; axes https://matplotlib.org/stable/api/axes_api.html. Verify backend availability in the actual environment.
