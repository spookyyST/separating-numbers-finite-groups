#!/usr/bin/env python3
"""Classify normalized size-7 windows in (C5)^3 up to linear symmetry.

A window is first translated to contain 0.  Since a line in F_5^3 has only
5 points, a 7-window has affine rank 2 or 3.

For rank 3, choose a basis from the six nonzero window points and send it to
(e1,e2,e3).  Thus every GL(3,5)-orbit occurs among
    {0,e1,e2,e3,a,b,c},
with C(121,3)=287,980 basis-normalized candidates.

For rank 2, similarly every orbit occurs among
    {0,e1,e2,a,b,c,d}
inside the standard plane, with C(22,4)=7,315 basis-normalized candidates.

Canonicalization over every basis contained in a candidate removes the remaining
duplication.  The expected exact counts are 3514 rank-3 orbits and 313 rank-2
orbits, for 3827 total normalized window types.

With --sat, each canonical representative is passed to the exact SAT solver from
search_abelian_examples.py.  Chunked SAT runs are partial searches only.
"""

from __future__ import annotations

import argparse
import itertools
import json
from itertools import islice
from pathlib import Path

P = 5


def det3(a, b, c):
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - b[0] * (a[1] * c[2] - a[2] * c[1])
        + c[0] * (a[1] * b[2] - a[2] * b[1])
    ) % P


def inv3_cols(a, b, c):
    d = det3(a, b, c)
    if d == 0:
        return None
    di = pow(d, -1, P)
    m00, m10, m20 = a
    m01, m11, m21 = b
    m02, m12, m22 = c
    return (
        ((m11*m22-m12*m21)*di % P,
         (m02*m21-m01*m22)*di % P,
         (m01*m12-m02*m11)*di % P),
        ((m12*m20-m10*m22)*di % P,
         (m00*m22-m02*m20)*di % P,
         (m02*m10-m00*m12)*di % P),
        ((m10*m21-m11*m20)*di % P,
         (m01*m20-m00*m21)*di % P,
         (m00*m11-m01*m10)*di % P),
    )


def matvec3(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) % P for i in range(3))


COORD_PERMS_3 = tuple(itertools.permutations(range(3)))


def canonical3(points):
    points = tuple(points)
    best = None
    for basis in itertools.combinations(points, 3):
        inv = inv3_cols(*basis)
        if inv is None:
            continue
        transformed = [matvec3(inv, v) for v in points]
        # Reordering the chosen basis corresponds to permuting coordinates.
        for perm in COORD_PERMS_3:
            key = tuple(sorted(tuple(v[i] for i in perm) for v in transformed))
            if best is None or key < best:
                best = key
    return best


def inv2_cols(a, b):
    d = (a[0] * b[1] - b[0] * a[1]) % P
    if d == 0:
        return None
    di = pow(d, -1, P)
    return (
        (b[1] * di % P, -b[0] * di % P),
        (-a[1] * di % P, a[0] * di % P),
    )


def matvec2(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(2)) % P for i in range(2))


def canonical2(points):
    points = tuple(points)
    best = None
    for basis in itertools.combinations(points, 2):
        inv = inv2_cols(*basis)
        if inv is None:
            continue
        transformed = [matvec2(inv, v) for v in points]
        for perm in ((0, 1), (1, 0)):
            key = tuple(sorted(tuple(v[i] for i in perm) for v in transformed))
            if best is None or key < best:
                best = key
    return best


def rank3_representatives():
    e1, e2, e3 = (1,0,0), (0,1,0), (0,0,1)
    all_nonzero = [v for v in itertools.product(range(P), repeat=3) if v != (0,0,0)]
    pool = [v for v in all_nonzero if v not in {e1,e2,e3}]
    keys = set()
    for tail in itertools.combinations(pool, 3):
        keys.add(canonical3((e1, e2, e3) + tail))
    return sorted(keys)


def rank2_representatives():
    e1, e2 = (1,0), (0,1)
    all_nonzero = [v for v in itertools.product(range(P), repeat=2) if v != (0,0)]
    pool = [v for v in all_nonzero if v not in {e1,e2}]
    keys = set()
    for tail in itertools.combinations(pool, 4):
        keys.add(canonical2((e1, e2) + tail))
    return sorted(keys)


def index3(v):
    # Matches itertools.product(range(5), repeat=3) used by group_table.
    return v[0] * 25 + v[1] * 5 + v[2]


def windows():
    rank3 = [(3, (0,) + tuple(index3(v) for v in rep)) for rep in rank3_representatives()]
    rank2 = [(2, (0,) + tuple(index3((v[0], v[1], 0)) for v in rep))
             for rep in rank2_representatives()]
    return rank3, rank2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sat", action="store_true",
                        help="exactly SAT-test the canonical representatives")
    parser.add_argument("--start", type=int, default=0,
                        help="start index in the combined representative list")
    parser.add_argument("--limit", type=int,
                        help="maximum representatives to SAT-test")
    parser.add_argument("--out", type=Path, default=Path("c5cubed_size7_certificate.json"))
    args = parser.parse_args()

    rank3, rank2 = windows()
    print(f"rank-3 GL(3,5) orbits: {len(rank3)}")
    print(f"rank-2 GL(2,5) orbits: {len(rank2)}")
    print(f"total normalized window types: {len(rank3)+len(rank2)}")

    if len(rank3) != 3514 or len(rank2) != 313:
        raise SystemExit("Unexpected orbit counts; audit the canonicalization before SAT testing.")

    if not args.sat:
        return

    from search_abelian_examples import group_table, solve_window, verify

    table = group_table((5,5,5))
    reps = rank3 + rank2
    stop = None if args.limit is None else args.start + args.limit
    selected = islice(enumerate(reps), args.start, stop)
    processed = 0

    for absolute_index, (rank, window) in selected:
        processed += 1
        f = solve_window(table, window)
        if f is not None:
            assert verify(table, window, f)
            result = {
                "factors": [5,5,5],
                "order": 125,
                "window_size": 7,
                "counting_lower_bound": 7,
                "normal_form_rank": rank,
                "representative_index": absolute_index,
                "window": list(window),
                "f": f,
            }
            print("FOUND", json.dumps(result))
            args.out.write_text(json.dumps(result, indent=2) + "\n")
            return
        if processed % 25 == 0:
            print(f"SAT-tested {processed} representatives in this chunk", flush=True)

    full = args.start == 0 and args.limit is None
    if full:
        print("EXHAUSTED all 3827 canonical window types: no size-7 separator exists.")
        print("Together with any verified size-8 certificate, this would prove sep_2((C5)^3)=8.")
    else:
        print("PARTIAL SAT search only; no nonexistence conclusion follows.")


if __name__ == "__main__":
    main()
