#!/usr/bin/env python3
"""Reduce normalized 5-windows in (C3)^3 modulo GL(3,3), then SAT-test them."""

from __future__ import annotations

import itertools

from search_abelian_examples import group_table, solve_window


POINTS = list(itertools.product(range(3), repeat=3))
INDEX = {point: i for i, point in enumerate(POINTS)}


def make_map(transform):
    return tuple(INDEX[transform(point)] for point in POINTS)


GENERATORS = []
for i in range(2):
    def swap(point, i=i):
        p = list(point)
        p[i], p[i + 1] = p[i + 1], p[i]
        return tuple(p)
    GENERATORS.append(make_map(swap))
for i in range(3):
    def scale(point, i=i):
        p = list(point)
        p[i] = 2 * p[i] % 3
        return tuple(p)
    GENERATORS.append(make_map(scale))
for source in range(3):
    for target in range(3):
        if source != target:
            def transvection(point, source=source, target=target):
                p = list(point)
                p[target] = (p[target] + p[source]) % 3
                return tuple(p)
            GENERATORS.append(make_map(transvection))


def orbit(seed: tuple[int, ...]):
    pending, result = [seed], {seed}
    while pending:
        window = pending.pop()
        for mapping in GENERATORS:
            image = tuple(sorted(mapping[x] for x in window))
            if image not in result:
                result.add(image)
                pending.append(image)
    return result


def main():
    all_windows = {(0,) + c for c in itertools.combinations(range(1, 27), 4)}
    representatives = []
    while all_windows:
        seed = next(iter(all_windows))
        current_orbit = orbit(seed)
        representatives.append(min(current_orbit))
        all_windows.difference_update(current_orbit)
    print(f"GL(3,3) reduces 14,950 normalized windows to {len(representatives)} representatives.")

    table = group_table((3, 3, 3))
    for number, window in enumerate(representatives, start=1):
        print(f"Testing representative {number}/{len(representatives)}: {window}", flush=True)
        f = solve_window(table, window)
        if f is not None:
            print(f"SAT: size-5 certificate exists: {window}")
            return
    print("UNSAT for every GL(3,3)-orbit: no normalized 5-window exists.")


if __name__ == "__main__":
    main()
