#!/usr/bin/env python3
"""Strengthened exact size-7 SAT search for G=(C5)^3.

This script imports the 3827 canonical size-7 windows from
``classify_c5cubed_windows.py`` and SAT-tests them with constraints that are
*necessary* for any separating binary 7-window on 125 points.

Why the extra constraints are valid
----------------------------------
A separating 7-window gives 125 distinct binary words out of the 128 words in
{0,1}^7, so exactly three words are missing.  Every coordinate is a translate
of the same Boolean colouring f, hence every coordinate has the same weight.
The three missing words are distinct, so after globally complementing f if
necessary we may assume |f^{-1}(1)|=63.  Then each coordinate is 1 in exactly
one of the three missing words, so the three missing supports partition the
seven coordinates.

Consequently, among the 125 observed words:

* any pair of coordinates has 31 or 32 simultaneous ones;
* any triple of coordinates has 15 or 16 simultaneous ones.

These conditions are logically implied by separation, so adding them can only
speed up UNSAT proofs.  Any SAT model is still directly verified before being
reported.
"""

from __future__ import annotations

import argparse
import itertools
import json
from itertools import islice
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.solvers import Cadical195

from classify_c5cubed_windows import windows
from search_abelian_examples import group_table, verify


N = 125


def add_exact_cardinality(solver, lits, bound, top_id):
    cnf = CardEnc.equals(lits=list(lits), bound=bound, top_id=top_id,
                         encoding=EncType.seqcounter)
    for clause in cnf.clauses:
        solver.add_clause(clause)
    return cnf.nv


def add_range_cardinality(solver, lits, lower, upper, top_id):
    lo = CardEnc.atleast(lits=list(lits), bound=lower, top_id=top_id,
                         encoding=EncType.seqcounter)
    for clause in lo.clauses:
        solver.add_clause(clause)
    hi = CardEnc.atmost(lits=list(lits), bound=upper, top_id=lo.nv,
                        encoding=EncType.seqcounter)
    for clause in hi.clauses:
        solver.add_clause(clause)
    return hi.nv


def solve_window_strong(table, window):
    """Return a verified Boolean colouring or None after an exact UNSAT decision."""
    next_var = N + 1

    with Cadical195() as solver:
        # Symmetry reduction: after complementing we may take weight(f)=63,
        # and after translating the colouring we may fix f(0)=1.
        solver.add_clause([1])
        top = add_exact_cardinality(solver, range(1, N + 1), 63, next_var - 1)
        next_var = top + 1

        # Exact separation constraints.  For every g != h, at least one
        # translated coordinate must differ.
        for g in range(N):
            for h in range(g + 1, N):
                differences = []
                for y in window:
                    a = table[g][y] + 1
                    b = table[h][y] + 1
                    z = next_var
                    next_var += 1
                    differences.append(z)
                    # z <=> (a XOR b)
                    solver.add_clause([-a, -b, -z])
                    solver.add_clause([a, b, -z])
                    solver.add_clause([a, -b, z])
                    solver.add_clause([-a, b, z])
                solver.add_clause(differences)

        # Near-full-cube necessary constraints for coordinate intersections.
        # For a subset J of window coordinates, create one AND variable per
        # group element g for the event that all selected coordinates are 1.
        # Pair intersections must be 31..32; triple intersections 15..16.
        for arity, lower, upper in ((2, 31, 32), (3, 15, 16)):
            for positions in itertools.combinations(range(len(window)), arity):
                and_vars = []
                for g in range(N):
                    inputs = [table[g][window[j]] + 1 for j in positions]
                    z = next_var
                    next_var += 1
                    and_vars.append(z)
                    # z <=> AND(inputs)
                    for lit in inputs:
                        solver.add_clause([-z, lit])
                    solver.add_clause([z] + [-lit for lit in inputs])
                top = add_range_cardinality(
                    solver, and_vars, lower, upper, next_var - 1
                )
                next_var = top + 1

        if not solver.solve():
            return None

        model = set(solver.get_model())
        f = [int(i + 1 in model) for i in range(N)]
        if not verify(table, window, f):
            raise RuntimeError("SAT solver returned a model that failed direct verification")
        return f


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--out", type=Path,
                        default=Path("c5cubed_size7_certificate.json"))
    parser.add_argument("--status-out", type=Path)
    args = parser.parse_args()

    rank3, rank2 = windows()
    reps = rank3 + rank2
    if len(rank3) != 3514 or len(rank2) != 313 or len(reps) != 3827:
        raise SystemExit("Unexpected orbit counts; audit classification first.")

    stop = len(reps) if args.limit is None else min(len(reps), args.start + args.limit)
    table = group_table((5, 5, 5))
    tested = 0

    for absolute_index, (rank, window) in islice(enumerate(reps), args.start, stop):
        tested += 1
        print(f"Testing {absolute_index}/{len(reps)-1}, rank {rank}: {window}", flush=True)
        f = solve_window_strong(table, window)
        if f is not None:
            result = {
                "factors": [5, 5, 5],
                "order": 125,
                "window_size": 7,
                "counting_lower_bound": 7,
                "normal_form_rank": rank,
                "representative_index": absolute_index,
                "window": list(window),
                "f": f,
            }
            args.out.write_text(json.dumps(result, indent=2) + "\n")
            print("FOUND", json.dumps(result))
            if args.status_out:
                args.status_out.write_text(json.dumps({
                    "start": args.start, "stop": stop, "tested": tested,
                    "result": "SAT", "representative_index": absolute_index,
                }, indent=2) + "\n")
            return

    full = args.start == 0 and stop == len(reps)
    status = {
        "start": args.start,
        "stop": stop,
        "tested": tested,
        "result": "UNSAT" if full else "PARTIAL_UNSAT",
    }
    if args.status_out:
        args.status_out.write_text(json.dumps(status, indent=2) + "\n")

    if full:
        print("EXHAUSTED all 3827 canonical window types: no size-7 separator exists.")
    else:
        print(f"Exact UNSAT on chunk [{args.start}, {stop}); global search remains incomplete.")


if __name__ == "__main__":
    main()
