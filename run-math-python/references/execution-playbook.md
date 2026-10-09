# Execution and evidence contract

Choose a script runner for a small deterministic experiment or a `.py` implementation. Choose a notebook for a paper reproduction whose mathematical discussion and outputs should stay together. Both require a concrete interpreter and actual execution logs. Read [routing.md](routing.md) for available library-to-subject pairings; dispatch by mathematical structure and precision need rather than by a keyword alone.

Run an authorized script with:

```bash
python scripts/run_math.py --script /absolute/job.py --out /absolute/new-run --python /absolute/env/bin/python --timeout 60 --seed 17 --package numpy --package scipy -- --self-test
```

This runner creates the output directory, snapshots the main source, captures stdout/stderr to files and records return code, timeout, versions and source hash in run.json. It runs the original script, so local module imports retain its script directory. Additional source modules and data need their own hashes. Reject an existing output directory instead of overwriting prior evidence. The runner controls process duration; it is not a security sandbox, and inherits the environment. POSIX timeout cleanup kills the separate process group; other platforms only kill the direct child and require platform-specific descendant cleanup.

For a notebook, install nbclient, nbformat and ipykernel in the intended environment, register that interpreter as a named kernel, and execute through `NotebookClient(nb, timeout=60, kernel_name=explicit_name).execute()`. Save the executed notebook. Verify the kernel's `sys.executable`, versions, working directory and RNG configuration in a first cell. Do not confuse a visually filled notebook with outputs generated during this run. A notebook execution failure must remain visible.

Worked evidence: a script prints JSON for 6*7. A completed exit and parsed value 42 establish this computation; a source snapshot permits inspection of the formula. They do not establish any theorem about arbitrary inputs. A script that exits seven after logging an error must return failed, and a sleeping script must return timeout. `--self-test` actually checks these runner paths in temporary directories.

Before handing a result back, distinguish supplied premises, code-derived values, numerical estimates and certificates checked by a specified verifier. A successful solver with NaN output, stale data, unsupported domain or unvalidated tolerance is not a successful mathematical task. Return unavailable if a library cannot be imported and a supported environment is not available.

Primary sources checked 2026-10-08: Python subprocess API https://docs.python.org/3/library/subprocess.html; Python virtual environments https://docs.python.org/3/library/venv.html; Jupyter nbclient execution https://nbclient.readthedocs.io/en/latest/client.html.

The bundled scripts/notebook_example.py constructs a temporary named kernel bound to the calling interpreter (IPC on POSIX, TCP elsewhere). It requires permitted local socket transport. In the current authoring environment both transports are restricted: this auxiliary notebook example has not executed successfully. Script execution is independently tested; never report a notebook as executed after a kernel startup failure.
