#!/usr/bin/env python3
"""Exact normalized size-7 search for sep_2((C5)^3).

Any 7-window can first be translated to contain 0.  Its affine span then has
rank 2 or 3 (rank 1 is impossible because a line in F_5^3 has only 5 points).

Rank 3: choose three members forming a basis and send them by GL(3,5) to
        e1,e2,e3.  It therefore suffices to test windows
        {0,e1,e2,e3,a,b,c}.  There are C(121,3)=287,980 such normalized
        candidates (with duplicates between GL-orbits allowed).

Rank 2: send a basis of the containing plane to e1,e2.  It therefore suffices
        to test windows {0,e1,e2,a,b,c,d} inside <e1,e2>.  There are
        C(22,4)=7,315 such candidates.

For every fixed window the SAT decision is exact.  Chunked runs are only partial
searches and must never be interpreted as a nonexistence proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
from itertools import islice
from math import comb
from pathlib import Path

from search_abelian_examples import group_table, solve_window, verify


FACTORS = (5, 5, 5)
ORDER = 125
WINDOW_SIZE = 7
RANK3_TOTAL = comb(121, 3)
RANK2_TOTAL = comb(22, 4)


def index_map():
    points = list(itertools.product(range(5), repeat=3))
    return points, {p: i for i, p in enumerate(points)}


def rank3_candidates():
    _, index = index_map()
    zero = index[(0, 0, 0)]
    e1 = index[(1, 0, 0)]
    e2 = index[(0, 1, 0)]
    e3 = index[(0, 0, 1)]
    base = (zero, e1, e2, e3)
    pool = [i for i in range(ORDER) if i not in base]
    for tail in itertools.combinations(pool, 3):
        yield base + tail


def rank2_candidates():
    points, index = index_map()
    zero = index[(0, 0, 0)]
    e1 = index[(1, 0, 0)]
    e2 = index[(0, 1, 0)]
    base = (zero, e1, e2)
    plane = [index[p] for p in points if p[2] == 0]
    pool = [i for i in plane if i not in base]
    for tail in itertools.combinations(pool, 4):
        yield base + tail


def run_family(name: str, generator, total: int, table, start: int, limit: int | None,
               progress: int, out: Path | None):
    stop = None if limit is None else start + limit
    candidates = islice(generator(), start, stop)
    processed = 0

    for absolute_index, window in enumerate(candidates, start=start):
        processed += 1
        f = solve_window(table, window)
        if f is not None:
            assert verify(table, window, f)
            result = {
                "factors": list(FACTORS),
                "order": ORDER,
                "window_size": WINDOW_SIZE,
                "counting_lower_bound": 7,
                "normal_form_rank": int(name[-1]),
                "candidate_index": absolute_index,
                "window": list(window),
                "f": f,
            }
            print("FOUND", json.dumps(result))
            if out is not None:
                out.write_text(json.dumps(result, indent=2) + "\n")
            return True

        if progress and processed % progress == 0:
            print(f"{name}: tested {processed:,} candidates in this chunk "
                  f"(absolute index {absolute_index:,}/{total-1:,})", flush=True)

    exhausted_full_family = start == 0 and limit is None
    if exhausted_full_family:
        print(f"EXHAUSTED {name}: all {total:,} normalized candidates are UNSAT.")
    else:
        end = start + processed
        print(f"PARTIAL {name}: tested indices [{start:,}, {end:,}); no certificate found. "
              "No nonexistence conclusion follows.")
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", choices=["2", "3", "both"], default="both")
    parser.add_argument("--start", type=int, default=0,
                        help="candidate index at which to start (useful for chunking)")
    parser.add_argument("--limit", type=int,
                        help="maximum candidates to test; omitted means exhaust family")
    parser.add_argument("--progress", type=int, default=100,
                        help="print progress every this many exact SAT decisions")
    parser.add_argument("--out", type=Path, default=Path("c5cubed_size7_certificate.json"))
    args = parser.parse_args()

    if args.start < 0 or (args.limit is not None and args.limit <= 0):
        raise SystemExit("--start must be nonnegative and --limit must be positive")

    table = group_table(FACTORS)

    families = []
    if args.rank in {"3", "both"}:
        families.append(("rank3", rank3_candidates, RANK3_TOTAL))
    if args.rank in {"2", "both"}:
        families.append(("rank2", rank2_candidates, RANK2_TOTAL))

    # For --rank both, --start/--limit apply independently to each family.  This
    # keeps chunking simple and explicit; use --rank 2 or --rank 3 for distributed runs.
    for name, generator, total in families:
        if args.start >= total:
            print(f"Skipping {name}: start index {args.start:,} >= {total:,} candidates.")
            continue
        if run_family(name, generator, total, table, args.start, args.limit,
                      args.progress, args.out):
            return


if __name__ == "__main__":
    main()
