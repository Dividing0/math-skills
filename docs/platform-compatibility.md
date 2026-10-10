# Platform compatibility

Issue [#10](https://github.com/Dividing0/math-skills/issues/10) adds native Windows verification to the existing Linux checks and also gates macOS compatibility. The audit covered all 59 skill Python helpers and the release packager, including their filesystem and subprocess boundaries. Python 3.14 remains the repository minimum; these checks do not establish compatibility with earlier interpreters.

## Verification scope

The [CI workflow](../.github/workflows/ci.yml) runs the same checks on Python 3.14 on `ubuntu-latest`, `windows-latest`, and `macos-latest`, with `fail-fast: false`. Every platform runs Ruff, Pyright, compilation of all tracked Python files, metadata/link validation, release packaging, and the regression suite. See each Actions job's setup logs for its actual OS image, architecture, and Python patch version; runner labels can change over time.

These environments were exercised on 10 October 2026. The [PR #11 checks](https://github.com/Dividing0/math-skills/pull/11/checks) record the latest results; the [initial native run](https://github.com/Dividing0/math-skills/actions/runs/38069776133) reproduced the Windows notebook cleanup failure described below.

| Environment | OS / architecture | Python |
| --- | --- | --- |
| Local checks | Linux x86-64, glibc 2.39 | CPython 3.14.7 |
| `ubuntu-latest` | Ubuntu 24.04.5, x86-64 | CPython 3.14.8 |
| `windows-latest` | Windows Server 2025, build 10.0.26100, x64 | CPython 3.14.7 |
| `macos-latest` | macOS 26.6.2, ARM64 | CPython 3.14.7 |

| Boundary | Actual regression coverage |
| --- | --- |
| Script entry points | `python <script> --help` for every skill helper and the packager |
| JSON file inputs | All 41 configurable helpers receive UTF-8 and UTF-8 BOM files, Unicode names, spaces, and a non-UTF-8 locale; source hashes must preserve Unicode |
| Lean file tools | Unicode source search, source hashes, native path containment, and checker validation |
| Process runner | Unicode script paths, literal spaces/quotes/ampersands in arguments, source snapshots, byte-preserving stdout/stderr, failure and timeout, and immediate log-directory rename |
| Checker processes | Real Python stand-in processes emit UTF-8 diagnostics; temporary Lean files must be closed before they can be opened by the process and removed afterward |
| Notebook | Real kernel bound to the current interpreter, temporary directories with Unicode/spaces, executed cells, saved notebook, and cleanup |
| Git and ZIP | NUL-delimited Unicode Git paths, CRLF skill frontmatter, UTF-8 metadata/resources, nested archive output, POSIX archive member names, unchanged resource bytes, extraction, and an extracted standalone helper |

For the two Lean checker helpers, the JSON file test uses invalid requests to verify decoding and validation without requiring Lake. Checker process tests replace only the external executable, so they establish process/file compatibility, not Lean proof correctness. The existing integration tests run the actual checker only when Elan, Lake, and an installed Lean 4 toolchain are available. They do not download toolchains.

The legacy-locale tests disable Python's UTF-8 mode and set the text locale to `C` *after* interpreter startup, preserving native filesystem encoding. CI explicitly uses UTF-8 for standard streams; this does not change file decoding. This verifies that enabling UTF-8 mode cannot hide accidental locale-dependent file reads.

## Confirmed fixes

- Repository metadata, Markdown, Lean sources/toolchain pins, and generated execution metadata use explicit UTF-8 file encoding. JSON input files additionally accept a UTF-8 BOM, including files written by Windows PowerShell's `Set-Content -Encoding utf8`.
- Checker stdout/stderr are decoded as UTF-8, with replacement for incomplete or invalid diagnostic bytes. Timeout diagnostics retain the same policy.
- The plot example writes relative to the working directory instead of requiring `/tmp`.
- The workflow specifies Bash for shell steps, uses the Python shell for syntax checking, and supplies the archive path through a quoted environment variable. It does not rely on PowerShell interpreting Bash heredocs or variable syntax.
- ZIP fixtures write deliberate LF bytes; another fixture deliberately uses CRLF. Packaging retains the checked-out resource bytes rather than normalizing them.
- Installing the notebook dependencies exposed a Pyright private-import error. `KernelManager` now comes from its public `jupyter_client.manager` module.
- Native Windows CI reproduced `WinError 32` when a live notebook kernel held the temporary working directory open. The notebook helper now explicitly asks nbclient to shut down its externally supplied kernel manager and channels before removing that directory. POSIX also closes the kernel instead of leaving it alive until process exit.

## Running on Windows

Use a Python 3.14 environment with the dependencies needed by the selected skill. Run helpers through the interpreter rather than their Unix executable bits:

```powershell
python research-number-theory/scripts/integer_tools.py --example | Set-Content -Encoding utf8 crt.json
python research-number-theory/scripts/integer_tools.py --input crt.json
python scripts/release_skills.py --output "$env:TEMP/math-skills.zip"
```

Paths in JSON are JSON strings: use forward slashes (`C:/work/input.json`) or escape backslashes (`C:\\work\\input.json`). Quote paths with spaces at the shell boundary. Package creation requires Git on `PATH` and a Git checkout; extracted skill helpers work without the repository's root tooling.

Input files must be UTF-8, optionally with a BOM; UTF-16 files are not accepted. Standard input/output follow Python's configured stream encoding. For redirected Unicode streams, set `$env:PYTHONIOENCODING = 'utf-8'`. Runner `stdout.txt` and `stderr.txt` preserve the child program's bytes; their encoding is chosen by that child, rather than converted by the runner.

## Limits

- CI provisions PyYAML, SymPy, NumPy, SciPy, NetworkX, statsmodels, matplotlib, Z3, PySCIPOpt, and the notebook runtime. Self-tests for other scientific examples run only if their dependencies are installed; explicit missing-dependency results are recorded as skips. Native execution of python-control, python-flint, GUDHI, SageMath, JAX, PyMC/ArviZ, CVXPY, and FEniCSx is not established by the default CI environment.
- Elan/Lake and Lean 4 are not provisioned by this matrix. A skipped real-checker integration test does not establish Lean toolchain compatibility.
- A host that prohibits local sockets cannot run a notebook kernel. The regression reports that specific restriction as a skip; native CI runners must execute it when sockets are available.
- On Windows, the process runner terminates the direct child on timeout; it does not promise termination of descendant processes. POSIX uses a process group. This existing behavior is unchanged.
- ZIP paths are portable, but archive byte identity across checkouts is not promised: Git newline conversion, file metadata, and ZIP timestamps may differ. No release is published by the CI matrix.
- Desktop Windows 10/11, Windows ARM64, alternative Python implementations, older Python versions, network shares, paths beyond platform limits, and unavailable optional native dependencies have not been verified.
