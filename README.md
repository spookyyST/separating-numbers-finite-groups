# Binary separating patterns in finite groups

[![License: MIT](https://img.shields.io/github/license/spookyyST/separating-numbers-finite-groups)](LICENSE)

This repository contains proof drafts, exact computational certificates, and
reproducible verification programs for the separating-pattern parameter of
Kang and Hsieh.

**Primary reference:** M.-H. Kang and Y.-H. Hsieh, *Information and Locality
in Cayley Graphs*, [arXiv:2608.04608](https://arxiv.org/abs/2608.04608), 2026.

## Preprint

The current preprint draft is available in [`paper/separating_patterns_preprint_v1.md`](paper/separating_patterns_preprint_v1.md), with LaTeX source in [`paper/separating_patterns_preprint_v1.tex`](paper/separating_patterns_preprint_v1.tex).

## Main results in this package

1. For all cyclic groups \(C_N\),
   \[
   \operatorname{sep}_q(C_N)=\lceil\log_q N\rceil.
   \]
   See `cyclic_groups_question_7_3_proof_draft.md`.

2. For the elementary abelian binary groups \(V_d=(C_2)^d\),
   \[
   \operatorname{sep}_2(V_d)=
   \begin{cases}
   3,&d=2,\\
   5,&d=4,\\
   d,&\text{otherwise}.
   \end{cases}
   \]
   See `elementary_abelian_2_groups_results.md`.

3. \((C_3)^3\) is a binary counterexample to attainment of the information
   bound:
   \[
   \operatorname{sep}_2((C_3)^3)=6>\lceil\log_2 27\rceil=5.
   \]
   See `c3cubed_counterexample.md`.

4. \((C_3)^4\) attains its binary counting lower bound:
   \[
   \operatorname{sep}_2((C_3)^4)=7.
   \]
   See `c3four_exact_result.md` and `c3four_size7_certificate.json`.

5. Every one of the 51 groups of order 32 has \(\operatorname{sep}_2(G)=5\).
   Explicit certificates are in `order32_sep_certificates.json`.

Literature priority has not yet been established.

## Requirements

- Python 3.10 or newer;
- [PySAT](https://pysathq.github.io/):

  ```bash
  python3 -m pip install -r requirements.txt
  ```

- GAP with the SmallGrp library is needed only for the order-32 verification.
  The commands below assume `gap` is on the PATH and that its library root is
  supplied explicitly when required.

## Reproduce the finite checks

```bash
python3 verify_f2_6.py
```

This checks the exceptional dimensions \(2,4\) and the explicit dimension-six
seed for \((C_2)^d\).

Expected output:

```text
Verified: sep_2(F_2^2) > 2, sep_2(F_2^4) > 4, sep_2(F_2^6) = 6
```

```bash
python3 classify_c3cubed_windows.py
```

This reduces all 14,950 normalized five-windows of \((C_3)^3\) to ten
automorphism orbits and proves each corresponding SAT instance unsatisfiable.

```bash
python3 verify_abelian_certificate.py c3xc3xc3_size6_certificate.json
python3 verify_abelian_certificate.py c3four_size7_certificate.json
```

These directly verify the stored upper-bound certificates for \((C_3)^3\) and
\((C_3)^4\).

To verify the order-32 certificates, supply paths to a GAP executable and its
library root:

```bash
python3 verify_order32_certificates.py \
  --gap /path/to/gap \
  --gap-root /path/to/gap-root
```

## Repository map

- `paper/`: current preprint sources;
- `binary_separating_patterns_note.md`: concise research-note draft;
- `RESEARCH_PACKAGE_OVERVIEW.md`: status and file guide;
- `c3four_exact_result.md`: exact result and certificate description for \((C_3)^4\);
- `search_abelian_examples.py`: generic SAT search for selected abelian groups;
- `search_order32_sep.py`: certificate search for the GAP SmallGroups of order 32;
- `classify_c3cubed_windows.py`: orbit reduction and SAT proof for \((C_3)^3\);
- `verify_abelian_certificate.py`: direct verifier for the stored abelian group certificates;
- `verify_order32_certificates.py`: independent checker for all stored order-32 certificates.

## Scope and open problems

The package does not claim a classification of all finite groups. In particular,
\((C_5)^3\) remains unresolved in this project. Structural classification of the
binary defect is also open.

## License and citation

The code and accompanying materials are released under the [MIT License](LICENSE).
If you use this repository, please cite it using `CITATION.cff`.
