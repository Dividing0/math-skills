"""Check new helpers against analytic answers and failures of their assumptions."""

import itertools
import json
import math
import shutil
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

from test_host_helpers import ROOT, load

MATH_HELPERS = {
    "solve-with-z3": "solve_smt.py",
    "optimize-with-scip": "solve_milp.py",
    "simulate-stochastic-differential-equations": "simulate_gbm.py",
    "solve-differential-algebraic-equations": "linear_dae.py",
    "compute-with-monte-carlo": "integrate_polynomial.py",
    "research-mathematical-cryptography": "finite_secrecy.py",
    "research-ergodic-theory": "finite_dynamics.py",
    "research-statistical-learning-theory": "finite_class_bound.py",
    "research-stochastic-control": "finite_horizon_mdp.py",
}


class SolverChecks(unittest.TestCase):
    def test_smt_witness_and_unsat_core(self):
        tool = load("solve-with-z3", "solve_smt.py")
        sat = tool.compute(tool.EXAMPLE)
        self.assertEqual(sat["solver_status"], "sat")
        self.assertEqual(sat["assertion_evaluations"], ["True", "True"])
        unsat = tool.compute(
            {
                "smt2": "(declare-const x Int) (assert (> x 0)) (assert (< x 0)) (assert (< x 10))"
            }
        )
        self.assertEqual(unsat["solver_status"], "unsat")
        self.assertEqual(unsat["core_assertion_indices"], [0, 1])
        self.assertNotIn("model", unsat)
        with self.assertRaises(ValueError):
            tool.compute({"smt2": "(assert (= missing 1))"})
        import z3

        with (
            patch.object(z3.Solver, "check", return_value=z3.unknown),
            patch.object(
                z3.Solver, "reason_unknown", return_value="test resource limit"
            ),
        ):
            unknown = tool.compute(tool.EXAMPLE)
        self.assertEqual(unknown["solver_status"], "unknown")
        self.assertEqual(unknown["reason_unknown"], "test resource limit")
        self.assertNotIn("model", unknown)
        self.assertNotIn("core_assertion_indices", unknown)

    def test_smt_integer_and_bitvector_domains_differ(self):
        tool = load("solve-with-z3", "solve_smt.py")
        integer = tool.compute(
            {"smt2": "(declare-const x Int) (assert (= x 255)) (assert (= (+ x 1) 0))"}
        )
        byte = tool.compute(
            {
                "smt2": "(declare-const x (_ BitVec 8)) (assert (= x #xff)) (assert (= (bvadd x #x01) #x00))"
            }
        )
        self.assertEqual(integer["solver_status"], "unsat")
        self.assertEqual(byte["solver_status"], "sat")

    def test_milp_matches_exhaustive_enumeration(self):
        tool = load("optimize-with-scip", "solve_milp.py")
        result = tool.compute(tool.EXAMPLE)
        best = max(3 * x + 2 * y for x in range(11) for y in range(2) if 2 * x + y <= 4)
        self.assertEqual(result["solver_status"], "optimal")
        self.assertAlmostEqual(result["objective"], best)
        self.assertLess(result["max_feasibility_violation"], 1e-9)
        self.assertLess(result["max_integrality_residual"], 1e-9)
        self.assertAlmostEqual(result["relative_gap"], 0)

    def test_milp_infeasible_and_free_variable(self):
        tool = load("optimize-with-scip", "solve_milp.py")
        data = {
            "variables": [{"name": "x", "lower": None}],
            "objective": [1],
            "constraints": [{"coefficients": [1], "sense": ">=", "rhs": -3}],
        }
        self.assertAlmostEqual(tool.compute(data)["objective"], -3)
        data["constraints"].append({"coefficients": [1], "sense": "<=", "rhs": -4})
        result = tool.compute(data)
        self.assertEqual(result["solver_status"], "infeasible")
        self.assertEqual(result["solution_count"], 0)
        self.assertNotIn("solution", result)
        unbounded = tool.compute(dict(data, constraints=[]))
        self.assertEqual(unbounded["solver_status"], "unbounded")
        self.assertIsNone(unbounded["dual_bound"])
        self.assertIsNone(unbounded["relative_gap"])
        with self.assertRaises(ValueError):
            tool.compute(dict(tool.EXAMPLE, objective=[1]))


class StochasticNumerics(unittest.TestCase):
    def test_sde_coupling_and_conventions(self):
        tool = load("simulate-stochastic-differential-equations", "simulate_gbm.py")
        data = dict(tool.EXAMPLE, steps=32, paths=128)
        ito = tool.compute(data)
        self.assertEqual(ito, tool.compute(data))
        converted = tool.compute(dict(data, interpretation="stratonovich"))
        correction = data["diffusion"] ** 2 / 2
        self.assertAlmostEqual(converted["ito_drift"], data["drift"] + correction)
        self.assertAlmostEqual(
            converted["sample_exact_mean"] / ito["sample_exact_mean"],
            math.exp(correction),
        )
        self.assertLess(
            ito["levels"][1]["milstein_rmse"], ito["levels"][0]["milstein_rmse"]
        )

    def test_sde_constant_paths_and_invalid_grid(self):
        tool = load("simulate-stochastic-differential-equations", "simulate_gbm.py")
        result = tool.compute(
            dict(tool.EXAMPLE, drift=0, diffusion=0, paths=8, steps=4)
        )
        self.assertEqual(result["sample_exact_mean"], 1)
        self.assertEqual(result["sample_exact_standard_error"], 0)
        for level in result["levels"]:
            self.assertEqual(level["euler_rmse"], 0)
            self.assertEqual(level["milstein_rmse"], 0)
        self.assertIsNone(result["observed_strong_orders"]["euler_rmse"])
        with self.assertRaises(ValueError):
            tool.compute(dict(tool.EXAMPLE, steps=3))

    def test_linear_dae_against_closed_form(self):
        tool = load("solve-differential-algebraic-equations", "linear_dae.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertAlmostEqual(result["exact_terminal_x"][0], math.exp(-2))
        self.assertEqual(result["algebraic_initial"], [-1])
        self.assertGreater(result["observed_order"], 0.9)
        for level in result["levels"]:
            self.assertLess(level["max_algebraic_residual"], 1e-12)
            self.assertLess(level["max_discrete_differential_residual"], 1e-12)
            self.assertAlmostEqual(
                level["terminal_x"][0], (1 + 2 / level["steps"]) ** (-level["steps"])
            )

    def test_dae_rejects_inconsistent_and_singular_problems(self):
        tool = load("solve-differential-algebraic-equations", "linear_dae.py")
        for changes in (
            {"D": [[0]]},
            {"algebraic_initial": [0]},
            {"A": [[1]], "B": [[0]], "steps": 1},
        ):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                tool.compute(dict(tool.EXAMPLE, **changes))

    def test_monte_carlo_zero_variance_controls_and_pairs(self):
        tool = load("compute-with-monte-carlo", "integrate_polynomial.py")
        for method in ("antithetic", "control-variate"):
            result = tool.compute(
                {
                    "coefficients": [0, 1],
                    "method": method,
                    "samples": 128,
                    "control_coefficient": 1,
                    "seed": 31,
                }
            )
            self.assertAlmostEqual(result["estimate"], 0.5)
            self.assertAlmostEqual(result["standard_error"], 0)
            self.assertEqual(result["independent_units"], 128)
            self.assertEqual(
                result["function_evaluations"], 256 if method == "antithetic" else 128
            )
        data = dict(tool.EXAMPLE, samples=100, method="plain")
        self.assertEqual(tool.compute(data), tool.compute(data))
        with self.assertRaises(ValueError):
            tool.compute(dict(data, samples=1))


class MathematicalSubjects(unittest.TestCase):
    def test_perfect_secrecy_and_correctness_are_separate(self):
        tool = load("research-mathematical-cryptography", "finite_secrecy.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertTrue(result["perfect_secrecy"])
        self.assertTrue(result["decryptable_per_key"])
        biased = tool.compute(dict(tool.EXAMPLE, key_probabilities=["3/4", "1/4"]))
        self.assertFalse(biased["perfect_secrecy"])
        self.assertEqual(biased["max_pair_total_variation"], "1/2")
        constant = tool.compute({"encryption_table": [[0, 0]]})
        self.assertTrue(constant["perfect_secrecy"])
        self.assertFalse(constant["decryptable_per_key"])
        with self.assertRaises(ValueError):
            tool.compute(dict(tool.EXAMPLE, key_probabilities=[1, 1]))

    def test_ergodicity_does_not_imply_mixing(self):
        tool = load("research-ergodic-theory", "finite_dynamics.py")
        result = tool.compute({"permutation": [1, 0], "observable": [0, 2]})
        self.assertTrue(result["ergodic"])
        self.assertFalse(result["mixing"])
        self.assertEqual(result["orbit_time_averages"], ["1", "1"])
        self.assertEqual(result["space_average"], "1")
        identity = tool.compute({"permutation": [0, 1], "observable": [0, 2]})
        self.assertFalse(identity["ergodic"])
        supported = tool.compute(
            {"permutation": [0, 2, 1], "observable": [4, 0, 2], "weights": [1, 0, 0]}
        )
        self.assertTrue(supported["ergodic"])
        self.assertTrue(supported["mixing"])

    def test_ergodic_classification_requires_invariance(self):
        tool = load("research-ergodic-theory", "finite_dynamics.py")
        result = tool.compute(
            {"permutation": [1, 0], "observable": [0, 1], "weights": ["3/4", "1/4"]}
        )
        self.assertFalse(result["measure_preserving"])
        self.assertNotIn("ergodic", result)
        with self.assertRaises(ValueError):
            tool.compute({"permutation": [0, 0], "observable": [0, 1]})

    def test_learning_bound_comparator_and_assumptions(self):
        tool = load("research-statistical-learning-theory", "finite_class_bound.py")
        data = dict(tool.EXAMPLE, losses=[[0] * 100, [1] * 100], class_size=10)
        result = tool.compute(data)
        self.assertAlmostEqual(result["uniform_radius"], math.sqrt(math.log(400) / 200))
        self.assertEqual(result["selected_hypothesis"], 0)
        self.assertEqual(result["risk_intervals"][0][0], 0)
        self.assertLess(
            tool.compute(dict(data, class_size=2))["uniform_radius"],
            result["uniform_radius"],
        )
        self.assertTrue(
            math.isfinite(tool.compute(dict(data, delta=5e-324))["uniform_radius"])
        )
        for changes in (
            {"iid": False},
            {"class_fixed_before_data": False},
            {"class_size": 1},
            {"losses": [[0.5]]},
        ):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                tool.compute(dict(data, **changes))

    def test_mdp_discount_and_terminal_time(self):
        tool = load("research-stochastic-control", "finite_horizon_mdp.py")
        data = {
            "transitions": [[[1]]],
            "costs": [[2]],
            "terminal_costs": [3],
            "horizon": 2,
            "discount": "1/2",
        }
        result = tool.compute(data)
        self.assertEqual(result["values_by_time"], [["15/4"], ["7/2"], ["3"]])
        self.assertEqual(result["policy_by_time"], [[0], [0]])
        terminal = tool.compute(dict(data, horizon=0))
        self.assertEqual(terminal["values_by_time"], [["3"]])
        self.assertEqual(terminal["policy_by_time"], [])
        with self.assertRaises(ValueError):
            tool.compute(dict(data, transitions=[[["1/2"]]]))

    def test_mdp_against_all_time_dependent_policies(self):
        tool = load("research-stochastic-control", "finite_horizon_mdp.py")
        data = {
            "transitions": [[["1/2", "1/2"], [0, 1]], [[1, 0], [0, 1]]],
            "costs": [[0, 1], [2, 0]],
            "terminal_costs": [0, 3],
            "horizon": 2,
            "discount": "3/4",
        }
        result = tool.compute(data)
        policy_values = []
        for actions in itertools.product(range(2), repeat=4):
            # Enumerate complete trajectories under each policy, independently of Bellman recursion.
            initial_values = []
            for start in range(2):
                expected = Fraction(0)
                for middle, end in itertools.product(range(2), repeat=2):
                    first, second = actions[start], actions[2 + middle]
                    probability = Fraction(
                        data["transitions"][start][first][middle]
                    ) * Fraction(data["transitions"][middle][second][end])
                    cost = (
                        data["costs"][start][first]
                        + Fraction(3, 4) * data["costs"][middle][second]
                        + Fraction(9, 16) * data["terminal_costs"][end]
                    )
                    expected += probability * cost
                initial_values.append(expected)
            policy_values.append(initial_values)
        self.assertEqual(
            list(map(Fraction, result["values_by_time"][0])),
            [min(v[s] for v in policy_values) for s in range(2)],
        )


class LeanWorkflows(unittest.TestCase):
    def test_migration_snapshot_records_pins_and_excludes_builds(self):
        tool = load("migrate-lean4-projects", "project_snapshot.py")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "lean-toolchain").write_text("leanprover/lean4:v4.29.1\n")
            (root / "Main.lean").write_text("example : True := True.intro\n")
            for excluded in (".lake", "build", "venv"):
                (root / excluded).mkdir()
                (root / excluded / "Generated.lean").write_text("-- ignored\n")
            (root / "Linked.lean").symlink_to(root / "Main.lean")
            before = tool.compute({"project": directory})
            process = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "migrate-lean4-projects/scripts/project_snapshot.py"),
                ],
                input=json.dumps({"project": directory}),
                text=True,
                capture_output=True,
                check=True,
                timeout=30,
            )
            self.assertEqual(json.loads(process.stdout)["result"], before)
            self.assertEqual(set(before["sources"]), {"Main.lean"})
            self.assertEqual(before, tool.compute({"project": directory}))
            (root / "lean-toolchain").write_text("leanprover/lean4:v4.30.0\n")
            (root / "Main.lean").unlink()
            (root / "New.lean").write_text("example : 1 = 1 := rfl\n")
            after = tool.compute({"project": directory})
            compared = tool.compute(
                {"operation": "compare", "before": before, "after": after}
            )
            self.assertEqual(
                compared["changes"]["configuration"]["changed"], ["lean-toolchain"]
            )
            self.assertEqual(compared["changes"]["sources"]["removed"], ["Main.lean"])
            self.assertEqual(compared["changes"]["sources"]["added"], ["New.lean"])

    def test_checker_timeout_is_not_an_expected_error(self):
        tool = load("test-lean4-code", "run_cases.py")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "lean-toolchain").write_text("test pin\n")
            (root / "Bad.lean").write_text("example : False := by exact True.intro\n")
            data = {
                "project": directory,
                "cases": [
                    {"file": "Bad.lean", "expect": "error", "contains": "type mismatch"}
                ],
            }
            preflight = subprocess.CompletedProcess([], 0, "Lean version", "")
            timeout = subprocess.TimeoutExpired(["lean"], 60, output=b"type mismatch")
            with patch.object(tool.subprocess, "run", side_effect=[preflight, timeout]):
                result = tool.compute(data)
            self.assertFalse(result["passed"])
            self.assertTrue(result["cases"][0]["timed_out"])
            for quote in ("'", "`"):
                warning = subprocess.CompletedProcess(
                    [], 0, f"warning: declaration uses {quote}sorry{quote}\n", ""
                )
                with patch.object(
                    tool.subprocess, "run", side_effect=[preflight, warning]
                ):
                    admitted = tool.compute(
                        dict(data, cases=[{"file": "Bad.lean", "expect": "success"}])
                    )
                self.assertFalse(admitted["passed"])
            with patch.object(
                tool.subprocess,
                "run",
                return_value=subprocess.CompletedProcess([], 1, "type mismatch", ""),
            ):
                unavailable = tool.compute(data)
            self.assertFalse(unavailable["passed"])
            self.assertEqual(unavailable["cases"], [])
            with (
                patch.object(tool.subprocess, "run", return_value=preflight),
                self.assertRaises(ValueError),
            ):
                tool.compute(
                    dict(data, cases=[{"file": "../outside.lean", "expect": "success"}])
                )

    @unittest.skipUnless(
        shutil.which("lake") and shutil.which("elan"), "Lake/Elan is unavailable"
    )
    def test_actual_lean_extensions_and_regressions(self):
        tool = load("test-lean4-code", "run_cases.py")
        listing = subprocess.run(
            ["elan", "toolchain", "list"], text=True, capture_output=True, check=True
        )
        pins = [
            line.split()[0]
            for line in listing.stdout.splitlines()
            if line.startswith("leanprover/lean4:")
        ]
        if not pins:
            self.skipTest("No Lean 4 toolchain installed")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "lean-toolchain").write_text(pins[0] + "\n")
            (root / "lakefile.toml").write_text('name = "expansion_tests"\n')
            (root / "Tests").mkdir()
            for name in ("Positive", "Negative"):
                shutil.copyfile(
                    ROOT / f"test-lean4-code/assets/{name}.lean",
                    root / f"Tests/{name}.lean",
                )
            shutil.copyfile(
                ROOT / "metaprogram-lean4/assets/Extensions.lean",
                root / "Extensions.lean",
            )
            with (root / "Extensions.lean").open("a") as stream:
                stream.write("\n#print axioms MetaprogramExample.generated_identity\n")
            data = dict(tool.EXAMPLE, project=directory)
            data["cases"] = data["cases"] + [
                {"file": "Extensions.lean", "expect": "success"}
            ]
            process = subprocess.run(
                [sys.executable, str(ROOT / "test-lean4-code/scripts/run_cases.py")],
                input=json.dumps(data),
                text=True,
                capture_output=True,
                check=True,
                timeout=240,
            )
            result = json.loads(process.stdout)["result"]
            self.assertTrue(result["passed"], result)
            self.assertIn(
                "does not depend on any axioms", result["cases"][-1]["stdout"]
            )
            (root / "Admitted.lean").write_text("example : False := by sorry\n")
            failures = tool.compute(
                {
                    "project": directory,
                    "cases": [
                        {"file": "Admitted.lean", "expect": "success"},
                        {
                            "file": "Tests/Positive.lean",
                            "expect": "error",
                            "contains": "type mismatch",
                        },
                    ],
                }
            )
            self.assertFalse(failures["passed"])
            self.assertTrue(all(not case["passed"] for case in failures["cases"]))


class ExpandedCLI(unittest.TestCase):
    def test_mathematical_examples_execute_as_documented(self):
        for skill, filename in MATH_HELPERS.items():
            with self.subTest(skill=skill):
                path = ROOT / skill / "scripts" / filename
                example = subprocess.run(
                    [sys.executable, str(path), "--example"],
                    text=True,
                    capture_output=True,
                    check=True,
                    timeout=30,
                )
                completed = subprocess.run(
                    [sys.executable, str(path), "--input", "-"],
                    input=example.stdout,
                    text=True,
                    capture_output=True,
                    check=True,
                    timeout=60,
                )
                payload = json.loads(completed.stdout)
                self.assertEqual(payload["status"], "completed")
                self.assertEqual(len(payload["input_sha256"]), 64)
                self.assertTrue(payload["evidence"])
                self.assertIn("python", payload["versions"])

    def test_cli_invalid_inputs_and_missing_solver(self):
        path = ROOT / "solve-with-z3/scripts/solve_smt.py"
        # In a fresh solver process, the first generated label is skill_assertion!0.
        # A caller's symbol with that name must not change satisfiability.
        collision = subprocess.run(
            [sys.executable, str(path)],
            input=json.dumps(
                {
                    "smt2": "(declare-const skill_assertion!0 Bool) (assert (not skill_assertion!0))"
                }
            ),
            text=True,
            capture_output=True,
            check=True,
            timeout=30,
        )
        self.assertEqual(json.loads(collision.stdout)["result"]["solver_status"], "sat")
        for source in ("[]", '{"timeout_ms": NaN}', "invalid json"):
            process = subprocess.run(
                [sys.executable, str(path)],
                input=source,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(process.returncode, 1)
            self.assertEqual(json.loads(process.stdout)["status"], "failed")
        missing = subprocess.run(
            [sys.executable, "-S", str(path)],
            input='{"smt2":"(assert true)"}',
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(missing.returncode, 3)
        self.assertEqual(json.loads(missing.stdout)["status"], "dependency_missing")


if __name__ == "__main__":
    unittest.main()
