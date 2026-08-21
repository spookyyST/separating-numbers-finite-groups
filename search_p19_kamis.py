#!/usr/bin/env python3
"""Build and verify the MIS instance for the C_19^3 size-13 search."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

P = 19
M = 13
STATES = 1 << M
MASK = (1 << P) - 1


def rotl(x: int) -> int:
    return ((x << 1) & MASK) | (x >> (P - 1))


def canonical(x: int) -> int:
    best = x
    y = x
    for _ in range(1, P):
        y = rotl(y)
        if y < best:
            best = y
    return best


def windows(x: int) -> tuple[int, ...]:
    bits = [(x >> i) & 1 for i in range(P)]
    out = []
    for a in range(P):
        v = 0
        for k in range(M):
            v = (v << 1) | bits[(a + k) % P]
        out.append(v)
    return tuple(out)


def generate_candidates():
    reps = []
    state_sets = []
    for x in range(1, (1 << P) - 1):
        if canonical(x) != x:
            continue
        ws = windows(x)
        if len(set(ws)) == P:
            reps.append(x)
            state_sets.append(ws)
    assert len(reps) == 27348, len(reps)
    return reps, state_sets


def build(out_graph: Path, out_reps: Path):
    reps, state_sets = generate_candidates()
    by_state = [[] for _ in range(STATES)]
    for j, ss in enumerate(state_sets):
        for v in ss:
            by_state[v].append(j)

    adj = []
    edge_twice = 0
    for j, ss in enumerate(state_sets):
        ngh = set()
        for v in ss:
            ngh.update(by_state[v])
        ngh.discard(j)
        row = sorted(ngh)
        adj.append(row)
        edge_twice += len(row)
    assert edge_twice % 2 == 0

    with out_graph.open("w") as f:
        f.write(f"{len(adj)} {edge_twice // 2}\n")
        for row in adj:
            f.write(" ".join(str(v + 1) for v in row) + "\n")
    out_reps.write_text(json.dumps(reps))
    print(f"built {len(reps)} candidates, {edge_twice // 2} conflict edges")


def check(graph: Path, reps_path: Path, solution: Path, output: Path | None):
    reps = json.loads(reps_path.read_text())
    labels = [int(x.strip()) for x in solution.read_text().splitlines() if x.strip()]
    if len(labels) != len(reps):
        raise SystemExit(f"solution has {len(labels)} labels, expected {len(reps)}")
    chosen = [i for i, value in enumerate(labels) if value != 0]

    all_states = []
    for i in chosen:
        all_states.extend(windows(reps[i]))
    if len(all_states) != P * len(chosen) or len(set(all_states)) != len(all_states):
        raise SystemExit("reported solution is not an independent cycle packing")

    result = {
        "size": len(chosen),
        "indices": chosen,
        "reps": [reps[i] for i in chosen],
        "target": P * P,
    }
    print(json.dumps({"size": result["size"], "target": result["target"]}))
    if output:
        output.write_text(json.dumps(result))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    b = sp.add_parser("build")
    b.add_argument("--graph", type=Path, default=Path("p19.graph"))
    b.add_argument("--reps", type=Path, default=Path("p19_reps.json"))
    c = sp.add_parser("check")
    c.add_argument("solution", type=Path)
    c.add_argument("--graph", type=Path, default=Path("p19.graph"))
    c.add_argument("--reps", type=Path, default=Path("p19_reps.json"))
    c.add_argument("--output", type=Path)
    args = ap.parse_args()
    if args.cmd == "build":
        build(args.graph, args.reps)
    else:
        check(args.graph, args.reps, args.solution, args.output)


if __name__ == "__main__":
    main()
