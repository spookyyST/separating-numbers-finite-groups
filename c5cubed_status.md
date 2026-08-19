# Current status of the binary separating number for `(C_5)^3`

Let `G=(C_5)^3`, so `|G|=125`. The binary counting bound is 7.

## Verified upper bound

The file `c5cubed_size8_certificate.json` contains an explicit binary colouring and an eight-element window. The generic direct verifier

```bash
python3 verify_abelian_certificate.py c5cubed_size8_certificate.json
```

checks that the 125 group elements produce 125 distinct eight-bit observation words. Therefore

\[
7\le \operatorname{sep}_2((C_5)^3)\le 8.
\]

The only remaining possibilities are 7 and 8.

## Exact reduction of the size-seven search

Every seven-element window can be translated to contain 0. A one-dimensional affine span is impossible because a line in `F_5^3` contains only five points. Hence the affine rank is 2 or 3.

### Rank 3

Choose three nonzero window points forming a basis. A `GL(3,5)` transformation sends them to the standard basis. It therefore suffices initially to consider windows

\[
\{0,e_1,e_2,e_3,a,b,c\}.
\]

Canonicalization over every basis contained in the six nonzero points gives exactly **3514** `GL(3,5)`-orbits.

### Rank 2

The same argument inside a plane reduces to windows

\[
\{0,e_1,e_2,a,b,c,d\}\subseteq \mathbb F_5^2.
\]

Canonicalization gives exactly **313** `GL(2,5)`-orbits.

Thus a complete exact size-seven decision requires only

\[
3514+313=3827
\]

canonical window types, rather than billions of raw windows.

The script `classify_c5cubed_windows.py` reproduces these orbit counts and can SAT-test the canonical representatives exactly. Chunked runs are explicitly reported as partial and do not imply nonexistence.

## Near-full-cube constraint

If a size-seven binary separator exists, its image consists of 125 of the 128 possible seven-bit words. Therefore exactly three words are missing. Because every observation coordinate is a translate of the same Boolean colouring, all seven coordinates have the same weight. Up to complementing the colouring, the missing words have exactly one `1` in each coordinate collectively: their supports partition the seven coordinates.

Consequently, for two selected translates of the `1`-set, their intersection size must be either 31 or 32. Which value occurs is determined by whether the corresponding two coordinates lie in the same missing-word support block.

These constraints are useful for pruning, but by themselves they do not yet decide whether a size-seven separator exists.

## Status

The exact value is not claimed yet. The remaining task is an exhaustive exact SAT decision over the 3827 canonical window types, or a human proof that rules out (or constructs) a size-seven separator.
