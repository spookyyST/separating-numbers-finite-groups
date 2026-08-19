# Near-full-cube rigidity for optimal binary separating patterns

This note records an elementary structural lemma that is useful when a finite
group has order only slightly below a power of two.

## Setup

Let `G` be a finite group with

\[
|G|=2^t-r,
\]

and suppose there is a binary separating pair `(f,Y)` with `|Y|=t`.
Write

\[
\Phi(g)=(f(gy))_{y\in Y}\in\{0,1\}^t.
\]

Since `Phi` is injective, its image contains `2^t-r` words, so exactly `r`
words of the binary cube are missing.  Let `M` be this set of missing words.

## The rigidity lemma

### Lemma

Every coordinate of the `r x t` binary matrix whose rows are the missing words
has the same column sum.

More precisely, if

\[
w=|f^{-1}(1)|,
\]

then every column of `M` contains exactly

\[
m=2^{t-1}-w
\]

ones.

### Proof

For every `y in Y`, the coordinate `g -> f(gy)` is a translate of `f` and
therefore has exactly `w` ones on `G`.  In the full binary cube, each coordinate
contains exactly `2^{t-1}` ones.  Hence the missing rows contain exactly
`2^{t-1}-w` ones in every coordinate.  This number is independent of the
coordinate.  \(\square\)

Complementing the colouring `f` complements every observed and missing word.
Thus `m` is replaced by `r-m`, and without loss of generality one may assume

\[
m\le r/2.
\]

## Higher intersections

For a nonempty coordinate set `J subseteq {1,...,t}`, let `n_J` be the number
of missing words which are `1` in every coordinate of `J`.  Then

\[
\#\{g\in G: f(gy)=1\text{ for every }y\in J\}
=2^{t-|J|}-n_J.
\]

This follows because exactly `2^{t-|J|}` words of the full binary cube have
ones on all coordinates in `J`, and precisely `n_J` of those words are missing.

This identity converts the combinatorics of the missing words into exact
multi-correlation constraints on translates of the single colouring `f`.

## Deficiency one: `r=1`

After complementing if needed, the unique missing word is

\[
0^t.
\]

Hence

\[
|f^{-1}(1)|=2^{t-1},
\]

and every nonempty selected coordinate set `J` has exactly

\[
2^{t-|J|}
\]

simultaneous ones.

## Deficiency two: `r=2`

After complementing, the common missing-column sum must be `m=1`; `m=0` would
make the two missing rows equal.  Therefore the two missing words are bitwise
complements.

Equivalently, the coordinates split into two blocks according to which missing
word contains the `1`.  For two selected coordinates, their simultaneous-one
count is

\[
2^{t-2}-1
\]

when the coordinates lie in the same block, and

\[
2^{t-2}
\]

when they lie in different blocks.

## Deficiency three: `r=3`

Again, after complementing, the common missing-column sum must be `m=1`.
Thus the supports of the three missing words are pairwise disjoint and together
cover all `t` coordinates.  At most one support may be empty, because the three
missing words are distinct.

For any nonempty coordinate set `J`, the simultaneous-one count among the
observed words is

\[
2^{t-|J|}-1
\]

if all coordinates in `J` lie in one missing-word support block, and

\[
2^{t-|J|}
\]

otherwise.

For `t=7` this gives the constraints used in the `(C_5)^3` search:

* pair intersections are `31` or `32`;
* triple intersections are `15` or `16`;
* fourfold intersections are `7` or `8`;
* fivefold intersections are `3` or `4`;
* sixfold intersections are `1` or `2`.

## Why this is useful

The lemma is group-independent.  It applies to every optimal binary separating
pattern whose image nearly fills the binary cube.  The group structure enters
only afterward, because these almost-uniform coordinate intersections must be
realized by translates of one and the same subset of `G`.

For `(C_5)^3`, `|G|=125=128-3`, so any hypothetical size-seven separator is
forced into the deficiency-three structure above.  This is the source of the
strong correlation restrictions used by `c5cubed_exact_search.py`.
