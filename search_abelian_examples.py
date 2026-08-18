#!/usr/bin/env python3
"""Find rigorous sep_2 certificates for selected finite abelian groups.

Each SAT answer is checked directly.  If the search limit is reached without
a certificate, the program reports INCONCLUSIVE — it never treats that as a
counterexample.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from math import prod
from pathlib import Path

from pysat.solvers import Cadical195


def group_table(factors: tuple[int, ...]) -> list[list[int]]:
    elements = list(itertools.product(*(range(m) for m in factors)))
    index = {x: i for i, x in enumerate(elements)}
    return [[index[tuple((a + b) % m for a, b, m in zip(x, y, factors))]
             for y in elements] for x in elements]


def lower_bound(n: int) -> int:
    return (n - 1).bit_length()


def solve_window(table: list[list[int]], window: tuple[int, ...], conflict_budget: int | None = None,
                 solver_class=Cadical195) -> list[int] | None:
    n = len(table)
    next_var = n + 1
    with solver_class() as solver:
        for g in range(n):
            for h in range(g + 1, n):
                differences = []
                for y in window:
                    a, b, z = table[g][y] + 1, table[h][y] + 1, next_var
                    next_var += 1
                    differences.append(z)
                    solver.add_clause([-a, -b, -z])
                    solver.add_clause([a, b, -z])
                    solver.add_clause([a, -b, z])
                    solver.add_clause([-a, b, z])
                solver.add_clause(differences)
        if conflict_budget is None:
            solved = solver.solve()
        else:
            solver.conf_budget(conflict_budget)
            solved = solver.solve_limited()
        if solved is not True:
            return None
        model = set(solver.get_model())
        return [int(i + 1 in model) for i in range(n)]


def verify(table: list[list[int]], window: tuple[int, ...], f: list[int]) -> bool:
    return len({tuple(f[table[g][y]] for y in window) for g in range(len(table))}) == len(table)


def random_certificate(table: list[list[int]], window: tuple[int, ...], attempts: int, rng: random.Random):
    """Fast heuristic for finding an upper-bound certificate; every hit is verified."""
    for _ in range(attempts):
        f = [rng.randrange(2) for _ in range(len(table))]
        if verify(table, window, f):
            return f
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("factors", nargs="+", type=int, help="e.g. 6 6 for C6 x C6")
    parser.add_argument("--windows", type=int, default=200,
                        help="number of candidate windows; stopping here is INCONCLUSIVE")
    parser.add_argument("--seed", type=int, default=20260818)
    parser.add_argument("--random-attempts", type=int, default=0,
                        help="try this many random functions per window before SAT")
    parser.add_argument("--no-sat", action="store_true",
                        help="do not fall back to SAT after the random attempts")
    parser.add_argument("--conflicts", type=int,
                        help="maximum SAT conflicts per window; an exhausted budget is inconclusive")
    parser.add_argument("--out", type=Path)
    parser.add_argument("--size", type=int, help="window size; defaults to the counting lower bound")
    args = parser.parse_args()

    factors = tuple(args.factors)
    table = group_table(factors)
    n, k = len(table), lower_bound(len(table))
    t = args.size if args.size is not None else k
    if t < k or t > n:
        raise SystemExit(f"Window size must lie between {k} and {n}.")
    if n > 128:
        raise SystemExit("This generic SAT encoding is intentionally limited to |G| <= 128.")
    candidates = [(0,) + x for x in itertools.combinations(range(1, n), t - 1)]
    random.Random(args.seed).shuffle(candidates)
    rng = random.Random(args.seed + 1)
    for count, window in enumerate(candidates[:args.windows], start=1):
        f = random_certificate(table, window, args.random_attempts, rng)
        if f is None and not args.no_sat:
            f = solve_window(table, window, args.conflicts)
        if f is not None:
            assert verify(table, window, f)
            certificate = {"factors": factors, "order": n, "window_size": t,
                           "counting_lower_bound": k,
                           "window": window, "f": f, "windows_tested": count}
            print("FOUND", json.dumps(certificate))
            if args.out:
                args.out.write_text(json.dumps(certificate, indent=2) + "\n")
            return
    print(f"INCONCLUSIVE after {args.windows} windows; no mathematical conclusion follows.")


if __name__ == "__main__":
    main()
