# Research package: separating patterns in finite groups

**Status date:** 20 August 2026  
**Author:** Igor Tomilson, independent researcher

This file is the entry point for the current research package. It separates
proved results, exact computational results, and open conjectures. Claims of
global novelty remain subject to a literature review and expert feedback.

## 1. Proven mathematical results

### Cyclic groups

For every \(q\ge2\) and \(N\ge2\),

\[
\operatorname{sep}_q(C_N)=\lceil\log_qN\rceil.
\]

The proof uses cut-down de Bruijn words.

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
dimensions and a two-dimensional lifting lemma. The cases \(d=2,4,6\) have
finite reproducible checks.

**Document:** `elementary_abelian_2_groups_results.md`.  
**Verifier:** `verify_f2_6.py`.

## 2. Exact computational results

### All groups of order 32

For all 51 GAP SmallGroups of order 32,

\[
\operatorname{sep}_2(G)=5.
\]

Each result has an explicit window and Boolean function certificate. The
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
14,950 normalized windows to 10 orbits. Exact SAT instances for those ten
representatives are UNSAT; a size-six certificate supplies the upper bound.

**Document:** `c3cubed_counterexample.md`.  
**Orbit/SAT program:** `classify_c3cubed_windows.py`.  
**Upper-bound certificate:** `c3xc3xc3_size6_certificate.json`.

### Exact value for \((C_3)^4\)

For \(G=(C_3)^4\),

\[
\operatorname{sep}_2(G)=7.
\]

The counting bound is seven because \(2^6<81\le2^7\). The stored size-seven
certificate produces 81 pairwise distinct translated binary words, so the lower
bound is attained.

**Document:** `c3four_exact_result.md`.  
**Certificate:** `c3four_size7_certificate.json`.  
**Verifier:** `verify_abelian_certificate.py`.

### Exact value for \((C_5)^3\)

For \(G=(C_5)^3\),

\[
\operatorname{sep}_2(G)=7,
\qquad
\delta_2(G)=0.
\]

The counting lower bound is seven because \(2^6<125\le2^7\). The stored
size-seven certificate produces 125 pairwise distinct translated binary words.
Its optimal seven-element window has affine rank two.

**Document:** `c5cubed_status.md`.  
**Certificate:** `c5cubed_size7_certificate.json`.  
**Verifier:** `verify_abelian_certificate.py`.

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

Certificates are stored in the correspondingly named JSON files. The generic SAT
search tool is `search_abelian_examples.py`.

## 3. What is *not* proved

The statement that only \((C_2)^2\) and \((C_2)^4\) have positive binary defect
is false because \((C_3)^3\) has defect one.

No classification of all finite groups, all abelian groups, or all elementary
abelian \(p\)-groups has yet been proved. The case \((C_5)^3\) is now resolved
by an explicit optimal certificate. No priority claim is made for the new
certificates until a broader literature check is completed.

## 4. Current research priorities

1. Look for structural constructions that explain why \((C_5)^3\) and
   \((C_3)^4\) attain the counting bound while \((C_3)^3\) does not.
2. Search the literature for equivalent Boolean-function or translate-code
   formulations.
3. Search further elementary abelian odd-prime cases for additional positive
   defect examples.
4. Determine whether the defect
   \[
   \delta_2(G)=\operatorname{sep}_2(G)-\lceil\log_2|G|\rceil
   \]
   can exceed one.
