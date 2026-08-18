#!/usr/bin/env python3
"""Verify every stored size-five certificate for GAP SmallGroups(32,i)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from search_order32_sep import DEFAULT_GAP, DEFAULT_GAP_ROOT, check_certificate, multiplication_table


ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gap", type=Path, default=DEFAULT_GAP)
    parser.add_argument("--gap-root", type=Path, default=DEFAULT_GAP_ROOT)
    parser.add_argument("--certificates", type=Path,
                        default=ROOT / "order32_sep_certificates.json")
    args = parser.parse_args()

    certificates = json.loads(args.certificates.read_text())
    expected_ids = [[32, group_id] for group_id in range(1, 52)]
    if [item.get("gap_id") for item in certificates] != expected_ids:
        raise SystemExit("Certificate file does not contain exactly GAP SmallGroup(32,1..51).")

    for item in certificates:
        group_id = item["gap_id"][1]
        _, table = multiplication_table(group_id, args.gap, args.gap_root)
        if not check_certificate(table, tuple(item["window"]), item["f"]):
            raise SystemExit(f"Invalid certificate for GAP SmallGroup(32,{group_id}).")
    print("Verified all 51 certificates: sep_2(G)=5 for every group of order 32.")


if __name__ == "__main__":
    main()
