# Research package: separating patterns in finite groups

**Status date:** 18 August 2026  
**Author:** Igor Tomilson, independent researcher

This file is the entry point for the current research package.  It separates
proved results, exact computational results, and open conjectures.  Claims of
global novelty remain subject to a literature review and expert feedback.

## 1. Proven mathematical results

### Cyclic groups

For every \(q\ge2\) and \(N\ge2\),

\[
\operatorname{sep}_q(C_N)=\lceil\log_qN\rceil.
\]

The proof uses cut-down de Bruijn words.  The same note gives the exact
connected and one-step parameters for the standard directed and undirected
cyclic Cayley graphs, and explains the connection with the cycle-packing
parameter \(M_q(m,k)\).

**Document:** `cyclic_groups_question_7_3_proof_draft.md`.

### Elementary abelian binary groups

For \(V_d=(C_2)^d\),

\[
\operatorname{sep}_2(V_d)=
\begin{cases}
3,&d=2,\\
5,&d=4,\\
d,&\text{otherwise}.
\end{cases}
\]

The infinite families follow from an explicit quadratic construction in odd
dimensions and a two-dimensional lifting lemma.  The cases \(d=2,4,6\) have
finite reproducible checks.

**Document:** `elementary_abelian_2_groups_results.md`.  
**Verifier:** `verify_f2_6.py`.

## 2. Exact computational results

### All groups of order 32

For all 51 GAP SmallGroups of order 32,

\[
\operatorname{sep}_2(G)=5.
\]

Each result has an explicit window and Boolean function certificate.  The
counting lower bound is 5, so each certificate proves equality.

**Search and verifier:** `search_order32_sep.py`.  
**Certificates:** `order32_sep_certificates.json`.

### A counterexample to the first universal hypothesis

For \(G=(C_3)^3\),

\[
\operatorname{sep}_2(G)=6,
\qquad
\lceil\log_2|G|\rceil=5.
\]

The size-five windows are reduced, by explicit linear automorphisms, from
14,950 normalized windows to 10 orbits.  Exact SAT instances for those ten
representatives are UNSAT; a size-six certificate supplies the upper bound.

**Document:** `c3cubed_counterexample.md`.  
**Orbit/SAT program:** `classify_c3cubed_windows.py`.  
**Upper-bound certificate:** `c3xc3xc3_size6_certificate.json`.

### Additional positive certificates

The following examples meet their binary counting lower bound:

\[
\operatorname{sep}_2(C_3^2)=4,
\quad \operatorname{sep}_2(C_5^2)=5,
\quad \operatorname{sep}_2(C_6^2)=6,
\quad
\operatorname{sep}_2(C_4^3)=6,
\quad \operatorname{sep}_2(C_8^2)=6.
\]

Certificates are stored in the correspondingly named JSON files.  The
generic SAT search tool is `search_abelian_examples.py`.

## 3. What is *not* proved

The statement that only \((C_2)^2\) and \((C_2)^4\) have positive binary
defect is false because \((C_3)^3\) has defect one.

No classification of all finite groups, all abelian groups, or all elementary
abelian \(p\)-groups has yet been proved.  In particular, the case
\((C_3)^4\) remains open in this project; an interrupted bounded SAT search
does not count as evidence either way.

## 4. Recommended external-email bundle

For Kang and Hsieh, send only the separating-pattern material:

1. `RESEARCH_PACKAGE_OVERVIEW.md`;
2. `cyclic_groups_question_7_3_proof_draft.md`;
3. `elementary_abelian_2_groups_results.md`;
4. `c3cubed_counterexample.md`;
5. `verify_f2_6.py` and `classify_c3cubed_windows.py`;
6. the two certificate files for order 32 and \((C_3)^3\).

## 5. Next research priorities

1. Independently audit the \((C_3)^3\) SAT calculation and preserve solver
   logs or proof certificates suitable for a paper.
2. Search the literature for the equivalent Boolean-function formulation.
3. Develop symmetry reduction for \((C_3)^4\) before attempting large SAT
   searches.
4. Ask Kang and Hsieh whether they recognize the \((C_3)^3\) phenomenon or
   an equivalent prior result.
