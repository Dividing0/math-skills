#!/usr/bin/env python3
"""Triangle persistence checked by boundary ranks over F2."""

if not __debug__:
    raise RuntimeError(
        "Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE."
    )

import argparse
import json
import math
import platform
import sys

p = argparse.ArgumentParser()
p.add_argument("--self-test", action="store_true")
args = p.parse_args()
try:
    import gudhi
except ImportError as exc:
    print(
        json.dumps(
            {"status": "dependency_missing", "dependency": "gudhi", "error": str(exc)}
        ),
        file=sys.stderr,
    )
    sys.exit(2)


def rank_f2(rows):
    a = [r[:] for r in rows]
    pivot = 0
    for col in range(len(a[0]) if a else 0):
        candidates = [r for r in range(pivot, len(a)) if a[r][col]]
        if not candidates:
            continue
        r = candidates[0]
        a[pivot], a[r] = a[r], a[pivot]
        for j in range(len(a)):
            if j != pivot and a[j][col]:
                a[j] = [v ^ w for v, w in zip(a[j], a[pivot])]
        pivot += 1
    return pivot


st = gudhi.SimplexTree()
for vertex in range(3):
    st.insert([vertex], filtration=0)
for edge in [[0, 1], [1, 2], [0, 2]]:
    st.insert(edge, filtration=1)
st.insert([0, 1, 2], filtration=2)
for simplex, value in st.get_filtration():
    for i in range(len(simplex)):
        face = simplex[:i] + simplex[i + 1 :]
        if face:
            assert st.filtration(face) <= value
st.compute_persistence(homology_coeff_field=2, persistence_dim_max=True)
h1 = st.persistence_intervals_in_dimension(1)
assert len(h1) == 1 and h1[0, 0] == 1 and h1[0, 1] == 2
r1 = rank_f2([[1, 0, 1], [1, 1, 0], [0, 1, 1]])
r2 = rank_f2([[1], [1], [1]])
assert r1 == 2 and r2 == 1
before = [3 - r1, 3 - r1]
after = [3 - r1, 3 - r1 - r2]
assert list(st.persistent_betti_numbers(1, 1))[:2] == before == [1, 1]
assert list(st.persistent_betti_numbers(2, 2))[:2] == after == [1, 0]
checks = [
    "filtration_face_order",
    "H1_birth_death",
    "boundary_ranks_F2",
    "betti_crosscheck",
]
if args.self_test:
    boundary = gudhi.SimplexTree()
    for edge in [[0, 1], [1, 2], [0, 2]]:
        boundary.insert(edge, filtration=1)
    boundary.compute_persistence(homology_coeff_field=2, persistence_dim_max=True)
    bars = boundary.persistence_intervals_in_dimension(1)
    assert len(bars) == 1 and math.isinf(bars[0, 1])
    checks.append("omitted_coface_changes_persistence")
print(
    json.dumps(
        {
            "status": "passed",
            "claim_status": "homology_of_specified_finite_filtered_complex",
            "python": platform.python_version(),
            "gudhi": gudhi.__version__,
            "coefficient_field": 2,
            "H1_intervals": h1.tolist(),
            "betti_before_fill": before,
            "betti_after_fill": after,
            "checks": checks,
        },
        allow_nan=False,
    )
)
