# Binary separating numbers for odd-prime rank-three groups

This note records exact binary separating numbers for several elementary abelian groups

\[
G_p=(C_p)^3
\]

and a simple cyclic-coset construction that connects the problem with fixed-length de Bruijn cycle packings. No claim of literature priority is made here.

## Exact verified values

The current verified values are

\[
\operatorname{sep}_2((C_3)^3)=6,
\]

while the information lower bound is attained for

\[
\operatorname{sep}_2((C_5)^3)=7,
\quad
\operatorname{sep}_2((C_7)^3)=9,
\quad
\operatorname{sep}_2((C_{11})^3)=11,
\quad
\operatorname{sep}_2((C_{13})^3)=12,
\quad
\operatorname{sep}_2((C_{17})^3)=13.
\]

The corresponding lower bounds are \(\lceil\log_2 p^3\rceil\), so the displayed certificates prove optimality.

The cases \(p=5,7,11,13,17\) therefore have binary defect zero, whereas \((C_3)^3\) has defect one.

## Cyclic-coset packing lemma

Let

\[
t=\lceil\log_2 p^3\rceil.
\]

Suppose \(t\le p\) and there exist \(p^2\) binary cyclic words

\[
w_{a,b}\in\{0,1\}^p,
\qquad (a,b)\in\mathbb F_p^2,
\]

such that all cyclic factors of length \(t\), taken over all starting positions and all \(p^2\) words, are pairwise distinct.

Then

\[
\operatorname{sep}_2((C_p)^3)=t.
\]

### Proof

Identify

\[
(C_p)^3\cong\mathbb F_p^3
\]

and let

\[
H=\{(i,0,0):i\in\mathbb F_p\}.
\]

The \(p^2\) cosets of \(H\) are indexed by \((a,b)\in\mathbb F_p^2\). Define a Boolean colouring by

\[
f(i,a,b)=w_{a,b}[i].
\]

Take the window

\[
Y=\{(0,0,0),(1,0,0),\ldots,(t-1,0,0)\}.
\]

The observation word at \((i,a,b)\) is exactly the cyclic length-\(t\) factor of \(w_{a,b}\) beginning at position \(i\). By hypothesis all \(p^3\) such factors are distinct. Thus \(Y\) is separating and has size \(t\). The counting lower bound gives equality. \(\square\)

Equivalently, the hypothesis is the fixed-length cycle-packing condition

\[
M_2(p,t)\ge p^2
\]

in the notation used for separating patterns. This is the same de Bruijn cycle-packing structure that appears in the fixed-length cycle literature.

## The case p = 7

Here

\[
t=\lceil\log_2 343\rceil=9>7,
\]

so the one-dimensional cyclic-coset lemma above cannot apply directly. A verified planar certificate instead uses the window

\[
Y=\{(0,j,0):0\le j\le6\}\cup\{(1,0,0),(1,1,0)\}.
\]

The stored Boolean colouring produces 343 pairwise distinct nine-bit observation words.

## The cases p = 11, 13, 17

For these primes the counting lengths are respectively

\[
11,\quad12,\quad13,
\]

all at most \(p\). Explicit cyclic-coset packings were converted into full Boolean certificates on \((C_p)^3\) and checked by the generic direct verifier.

The certificate files are

- `c11cubed_optimal_certificate.json`;
- `c13cubed_optimal_certificate.json`;
- `c17cubed_optimal_certificate.json`.

Together with `c7cubed_size9_certificate.json`, they can be checked with

```bash
python3 verify_abelian_certificate.py c7cubed_size9_certificate.json
python3 verify_abelian_certificate.py c11cubed_optimal_certificate.json
python3 verify_abelian_certificate.py c13cubed_optimal_certificate.json
python3 verify_abelian_certificate.py c17cubed_optimal_certificate.json
```

## Current conjectural picture

The verified data suggest the following natural question:

> Is \((C_3)^3\) the only group \((C_p)^3\), with \(p\) an odd prime, whose binary separating number exceeds the information lower bound?

This remains a conjectural direction. In particular, no general theorem for all odd primes is claimed here.
