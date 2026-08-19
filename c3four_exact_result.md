# Exact binary separating number for \((C_3)^4\)

Let
\[
G=(C_3)^4\cong \mathbb F_3^4.
\]
Then
\[
\boxed{\operatorname{sep}_2(G)=7.}
\]

## Lower bound

Since \(|G|=81\), every binary separating window of size \(t\) must satisfy
\[
2^t\ge 81.
\]
Because
\[
2^6=64<81\le128=2^7,
\]
we have
\[
\operatorname{sep}_2(G)\ge7.
\]

## Explicit upper-bound certificate

The repository file `c3four_size7_certificate.json` stores a seven-element window
and a Boolean function on the 81 elements of \(\mathbb F_3^4\), using the same
lexicographic element ordering as `verify_abelian_certificate.py`.

The window indices are
\[
Y=(0,27,9,3,1,36,30).
\]
In coordinate notation these are
\[
(0,0,0,0),
(1,0,0,0),
(0,1,0,0),
(0,0,1,0),
(0,0,0,1),
(1,1,0,0),
(1,0,1,0).
\]

Run

```bash
python3 verify_abelian_certificate.py c3four_size7_certificate.json
```

The verifier directly checks that the 81 translated seven-bit words are pairwise distinct. Therefore
\[
\operatorname{sep}_2(G)\le7.
\]
Combining with the counting lower bound gives
\[
\boxed{\operatorname{sep}_2((C_3)^4)=7.}
\]

## Status

The certificate was found by heuristic local search, but the mathematical result does not rely on the heuristic: the stored certificate is directly checkable, and the lower bound is the information bound. A preliminary literature search has not located this exact value stated elsewhere; no priority claim is made here.
