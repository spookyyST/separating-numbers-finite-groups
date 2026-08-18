#!/usr/bin/env python3
"""Exact SAT search for sep_2(G)=5 for every GAP SmallGroup(32,i).

A recorded result is a certificate: for the GAP group ID, the printed window
and Boolean table make the translated-word map injective.  No random Boolean
functions are used.  Randomness, when enabled, only changes the order in
which candidate windows are tested.

Requires: GAP with the SmallGrp package and python-sat.
"""

from __future__ import annotations

import argparse
import ast
import itertools
import json
import random
import subprocess
from pathlib import Path

from pysat.solvers import Cadical195


ROOT = Path(__file__).resolve().parent
DEFAULT_GAP = ROOT / ".tools" / "build-gap" / "gap"
DEFAULT_GAP_ROOT = ROOT / ".tools" / "src" / "gap-4.14.0"
N = 32


def multiplication_table(group_id: int, gap: Path, gap_root: Path):
    """Return GAP's structure description and a 0-based multiplication table."""
    program = f'''G := SmallGroup(32,{group_id});;
e := Concatenation([One(G)], Filtered(Elements(G), x -> x <> One(G)));;
t := List([1..32], a -> List([1..32], b -> Position(e,e[a]*e[b])-1));;
Print(StructureDescription(G),"\\n");;
Print(t,"\\n");;
QUIT;'''
    result = subprocess.run(
        [str(gap), "-l", str(gap_root), "-q", "-c", program],
        check=True,
        capture_output=True,
        text=True,
    )
    description, separator, table_text = result.stdout.partition("\n")
    if not separator:
        raise RuntimeError(f"Unexpected GAP output for group {group_id}: {result.stdout!r}")
    return description, ast.literal_eval(table_text)


def solve_window(table: list[list[int]], window: tuple[int, ...]):
    """Find f for this window, or return None after an exhaustive SAT decision."""
    # Variables 1..32 encode f(0),...,f(31).  The remaining variables encode
    # f(g*y) XOR f(h*y) for each pair g<h and each y in the window.
    next_var = N + 1
    with Cadical195() as solver:
        for g in range(N):
            for h in range(g + 1, N):
                difference_vars = []
                for y in window:
                    a = table[g][y] + 1
                    b = table[h][y] + 1
                    z = next_var
                    next_var += 1
                    difference_vars.append(z)
                    # z <=> (a XOR b)
                    solver.add_clause([-a, -b, -z])
                    solver.add_clause([a, b, -z])
                    solver.add_clause([a, -b, z])
                    solver.add_clause([-a, b, z])
                # The words at g and h must differ somewhere.
                solver.add_clause(difference_vars)
        if not solver.solve():
            return None
        model = set(solver.get_model())
        return [int(i + 1 in model) for i in range(N)]


def check_certificate(table: list[list[int]], window: tuple[int, ...], f: list[int]) -> bool:
    words = {tuple(f[table[g][y]] for y in window) for g in range(N)}
    return len(words) == N


def window_order(trials: int, seed: int):
    """First test randomly shuffled windows; then all remaining windows."""
    all_windows = [(0,) + c for c in itertools.combinations(range(1, N), 4)]
    rng = random.Random(seed)
    rng.shuffle(all_windows)
    if trials <= 0 or trials >= len(all_windows):
        return all_windows
    return itertools.chain(all_windows[:trials], all_windows[trials:])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=int, default=1)
    parser.add_argument("--last", type=int, default=51)
    parser.add_argument("--trials", type=int, default=300,
                        help="randomized windows tried first; the search then remains exhaustive")
    parser.add_argument("--seed", type=int, default=20260818)
    parser.add_argument("--gap", type=Path, default=DEFAULT_GAP)
    parser.add_argument("--gap-root", type=Path, default=DEFAULT_GAP_ROOT)
    parser.add_argument("--out", type=Path, default=ROOT / "order32_sep_certificates.json")
    args = parser.parse_args()

    if not args.gap.is_file():
        raise SystemExit(f"GAP executable not found: {args.gap}")
    results = []
    for group_id in range(args.first, args.last + 1):
        description, table = multiplication_table(group_id, args.gap, args.gap_root)
        print(f"[{group_id:02d}/51] {description}", flush=True)
        for tested, window in enumerate(window_order(args.trials, args.seed + group_id), start=1):
            f = solve_window(table, window)
            if f is not None:
                assert check_certificate(table, window, f)
                result = {
                    "gap_id": [32, group_id],
                    "structure_description": description,
                    "window": list(window),
                    "f": f,
                    "windows_tested": tested,
                }
                results.append(result)
                print(f"  FOUND after {tested} windows: Y={result['window']}", flush=True)
                break
        else:
            # This is rigorous: every normalized 5-element window was UNSAT.
            results.append({"gap_id": [32, group_id], "structure_description": description,
                            "status": "no window of size 5 exists"})
            print("  PROVED: no window of size 5 exists", flush=True)
        args.out.write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    main()
