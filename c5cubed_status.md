# Exact binary separating number for `(C_5)^3`

Let `G=(C_5)^3`, so `|G|=125`. The binary counting bound is

\[
\lceil\log_2 125\rceil=7.
\]

## Exact result

An explicit size-seven certificate is stored in
`c5cubed_size7_certificate.json`. Its window is

\[
Y=\{0,5,10,15,25,30,35\}.
\]

Under the standard identification used by `group_table((5,5,5))`, this is

\[
\{(0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,0),(1,2,0)\}.
\]

The generic direct verifier

```bash
python3 verify_abelian_certificate.py c5cubed_size7_certificate.json
```

checks that the 125 group elements produce 125 pairwise distinct seven-bit
observation words. Therefore the counting lower bound is attained:

\[
\boxed{\operatorname{sep}_2((C_5)^3)=7}.
\]

Equivalently, the binary defect is

\[
\boxed{\delta_2((C_5)^3)=0}.
\]

The colouring in the certificate has weight 63. With the coordinate order in
the stored window, the three missing words from the full seven-cube are

```text
0000000
0000111
1111000
```

Their supports have sizes `0,3,4`, in agreement with the near-full-cube
rigidity constraint.

## Structure of the certificate

The seven-element window has affine rank two: it lies in a copy of `(C_5)^2`
inside `(C_5)^3`. Thus the optimal separator does not require a rank-three
window.

This is useful structurally. The ambient group splits into five cosets of the
plane containing the window, and the certificate can be viewed as five
25-element observation packets whose union consists of 125 distinct words.

## Historical search reduction

Before the size-seven construction was found, normalized seven-windows were
reduced to 3514 rank-three and 313 rank-two `GL`-orbits, for 3827 canonical
window types. Further affine and local correlation reductions were useful for
search, but they are no longer needed to establish the exact value because the
explicit size-seven certificate attains the lower bound.

The old size-eight certificate remains a valid upper-bound certificate but is
no longer optimal.
