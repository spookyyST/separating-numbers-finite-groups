#!/usr/bin/env python3
"""Directly verify a stored Boolean separating certificate for an abelian group."""

from __future__ import annotations

import argparse
import itertools
import json
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def group_table(factors: tuple[int, ...]) -> list[list[int]]:
    elements = list(itertools.product(*(range(m) for m in factors)))
    index = {element: i for i, element in enumerate(elements)}
    return [[index[tuple((a + b) % m for a, b, m in zip(x, y, factors))]
             for y in elements] for x in elements]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path,
                        default=ROOT / "c3xc3xc3_size6_certificate.json")
    args = parser.parse_args()

    certificate = json.loads(args.certificate.read_text())
    factors = tuple(certificate["factors"])
    table = group_table(factors)
    order = prod(factors)
    if order != certificate["order"]:
        raise SystemExit("Certificate order disagrees with its factors.")

    window, f = tuple(certificate["window"]), certificate["f"]
    words = {tuple(f[table[g][y]] for y in window) for g in range(order)}
    if len(words) != order:
        raise SystemExit("Certificate is not separating.")
    print(f"Verified {args.certificate.name}: {order} distinct words from a window of size {len(window)}.")


if __name__ == "__main__":
    main()
