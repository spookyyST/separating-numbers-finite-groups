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


def expand_coloring(certificate: dict) -> list[int]:
    if "f" in certificate:
        return certificate["f"]

    if certificate.get("encoding") != "cyclic_coset_words":
        raise SystemExit("Certificate has neither f nor a supported compact encoding.")

    factors = tuple(certificate["factors"])
    if len(factors) != 3 or len(set(factors)) != 1:
        raise SystemExit("cyclic_coset_words requires factors [p,p,p].")
    p = factors[0]
    words = certificate["coset_words"]
    if len(words) != p * p:
        raise SystemExit("Compact certificate must contain exactly p^2 coset words.")

    f = [0] * (p ** 3)
    for a in range(p):
        for b in range(p):
            word = int(words[a * p + b])
            if word < 0 or word >= (1 << p):
                raise SystemExit("A compact coset word is outside the p-bit range.")
            for i in range(p):
                # itertools.product order indexes (i,a,b) as i*p^2 + a*p + b.
                f[i * p * p + a * p + b] = (word >> i) & 1
    return f


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

    window, f = tuple(certificate["window"]), expand_coloring(certificate)
    if len(f) != order:
        raise SystemExit("Certificate coloring length disagrees with group order.")

    words = {tuple(f[table[g][y]] for y in window) for g in range(order)}
    if len(words) != order:
        raise SystemExit("Certificate is not separating.")
    print(f"Verified {args.certificate.name}: {order} distinct words from a window of size {len(window)}.")


if __name__ == "__main__":
    main()
