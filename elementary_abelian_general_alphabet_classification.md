# Elementary abelian groups with prime-power alphabets

This note gives a complete classification for

\[
E_n(p)=(C_p)^n\cong \mathbb F_p^n
\]

when the alphabet has prime-power size

\[
q=p^r.
\]

The earlier field-sized-alphabet note is the special case `n=rd`.  No claim of
literature priority is made here.

## Main theorem

Let `p` be prime and `r,n>=1`.

### Odd characteristic

If `p` is odd, then

\[
\boxed{
\operatorname{sep}_{p^r}(E_n(p))=
\left\lceil\frac nr\right\rceil.
}
\]

Thus the information lower bound is always sharp.

### Characteristic two with at least four colours

If `p=2` and `r>=2`, then

\[
\boxed{
\operatorname{sep}_{2^r}(E_n(2))=
\begin{cases}
3,&n=2r,\\[1mm]
\left\lceil n/r\right\rceil,&n\ne2r.
\end{cases}
}
\]

So there is exactly one exceptional dimension for each non-binary power-of-two
alphabet.

### Binary alphabet

For `p=2,r=1`, the previously established binary theorem is

\[
\boxed{
\operatorname{sep}_2(E_n(2))=
\begin{cases}
3,&n=2,\\
5,&n=4,\\
n,&\text{otherwise}.
\end{cases}
}
\]

The binary alphabet therefore has one additional exceptional dimension, namely
`n=4`.

## 1. Counting lower bound

A window of size `t` produces at most

\[
(p^r)^t=p^{rt}
\]

observation words.  Since `|E_n(p)|=p^n`,

\[
\operatorname{sep}_{p^r}(E_n(p))
\ge
\left\lceil\frac nr\right\rceil.
\]

Write

\[
t=\left\lceil\frac nr\right\rceil.
\]

## 2. Odd characteristic: sharpness for every `n`

The case `t=1` is trivial: if `n<=r`, one colour can simply encode the entire
state injectively.

Assume `t>=2`.  Write the state coordinates as

\[
(p_1,\ldots,p_r; z),
\]

where the remaining `m=n-r` coordinates are partitioned into `t-1` nonempty
blocks, each of size at most `r`.  Denote the coordinate in block `i` and output
position `j` by `z_{i,j}` when it exists.

Define an `r`-component label

\[
f_j=p_j+\sum_i z_{i,j}^2.
\]

For each block `i`, let the window contain the direction which adds `1` to every
coordinate in that block.  The translated difference in output component `j` is

\[
(z_{i,j}+1)^2-z_{i,j}^2=2z_{i,j}+1
\]

when that coordinate exists.  Since `p` is odd, `2` is invertible.  Hence the
`t-1` translated differences recover every `z` coordinate.  The base label then
recovers all `p_j`.

The window has exactly `t` positions, proving sharpness of the counting bound.

## 3. Two-position windows in characteristic two

Assume `p=2`, `r>=1`, and

\[
r<n\le2r,
\]

so the counting lower bound is two.

Normalize a two-position window to

\[
\{0,y\},\qquad y\ne0.
\]

Since every nonzero element has additive order two, the group is partitioned into

\[
2^{n-1}
\]

orbits of the form

\[
\{x,x+y\}.
\]

If the two colours on such an orbit are `a,b`, the two observation words are
`(a,b)` and `(b,a)`.  Therefore `a` and `b` must be distinct, and different
orbits must receive different unordered colour pairs.

With `q=2^r` colours, the number of available unordered distinct colour pairs is

\[
\binom q2=\frac{q(q-1)}2.
\]

### The strict case `n<2r`

If `n<2r`, then

\[
2^{n-1}\le2^{2r-2}<2^{r-1}(2^r-1)=\binom{2^r}{2}.
\]

Thus there are enough unordered colour pairs.  Assign a different pair to each
orbit and orient it arbitrarily.  The resulting two-position observation map is
injective.  Hence

\[
\operatorname{sep}_{2^r}(E_n(2))=2
\]

whenever `r<n<2r`.

### The full case `n=2r`

Now the number of group orbits is

\[
2^{2r-1}=\frac{q^2}{2},
\]

which is strictly larger than

\[
\frac{q(q-1)}2.
\]

Hence a two-position separator is impossible.

For the matching upper bound, identify

\[
E_{2r}(2)\cong (\mathbb F_{2^r},+)^2
\]

and use

\[
f(a,b)=ab
\]

with the three-position window

\[
\{0,e_1,e_2\}.
\]

The two translated differences recover `b` and `a`.  Therefore

\[
\operatorname{sep}_{2^r}(E_{2r}(2))=3.
\]

This argument includes the binary exception `n=2`.

## 4. Characteristic two, `r>=2`, and at least three observations

Assume `r>=2` and

\[
t=\left\lceil n/r\right\rceil\ge3.
\]

Put

\[
s=t-1,
\qquad
m=n-r.
\]

Then

\[
s\le m\le rs.
\]

Write the state as

\[
(p,z),
\qquad
p\in\mathbb F_2^r,
\qquad
z\in\mathbb F_2^m.
\]

Choose the first `s` coordinates of `z` and call them

\[
a_1,\ldots,a_s.
\]

They will be the `s` nonzero window directions.  The remaining `m-s` coordinates
are called external variables.

We construct an `r`-bit quadratic map

\[
Q(z)=(Q_1(z),\ldots,Q_r(z))
\]

so that the `rs` derivative bits

\[
D_{a_i}Q_k
\]

recover all `m` coordinates of `z`.

### Internal coordinates when `s` is even

Put

\[
Q_1=a_1a_2+a_3a_4+\cdots+a_{s-1}a_s.
\]

The derivatives of `Q_1` in the `a_i` directions return the partner variables,
so together they recover every `a_i`.  Reserve these `s` derivative slots.

### Internal coordinates when `s` is odd

Put

\[
Q_1=a_1a_2+a_3a_4+\cdots+a_{s-2}a_{s-1},
\]

and

\[
Q_2=a_1a_s.
\]

The first `s-1` variables are recovered from derivatives of `Q_1`, while
`D_{a_1}Q_2=a_s`.  Again exactly `s` derivative slots are enough to recover all
internal direction variables.

### External coordinates

There are

\[
rs-s
\]

unreserved derivative slots and only

\[
m-s\le rs-s
\]

external variables.  Assign each external variable `w` to a distinct unreserved
slot `(i,k)` and add the term

\[
a_iw
\]

to `Q_k`.

The derivative in that slot is `w`, possibly plus an already recovered internal
variable.  Hence, after recovering the `a_i`, all external variables are recovered
one by one.

Finally define the label

\[
f(p,z)=p+Q(z)
\]

with bitwise addition in `F_2^r`, and use the window

\[
\{0,a_1,\ldots,a_s\}.
\]

The `s` translated differences recover `z`; the base colour then recovers `p`.
Thus the window of size `t` is separating, and the counting lower bound is sharp.

This proves

\[
\operatorname{sep}_{2^r}(E_n(2))=
\left\lceil n/r\right\rceil
\]

for every `r>=2` and every `n>2r`.

Together with Sections 2 and 3, this completes the non-binary characteristic-two
classification.

## 5. Why the binary alphabet has one more exception

The construction in Section 4 needs at least two output bits when the number of
nonzero window directions is odd.  For `r=1`, this extra output channel does not
exist.  The previously proved binary classification shows that exactly one further
failure occurs:

\[
\operatorname{sep}_2(E_4(2))=5
\]

instead of the counting value four.

For all other binary dimensions except `n=2`, the counting bound is attained.

## 6. Interpretation

For odd characteristic, elementary abelian groups never pay any structural cost
beyond information counting, regardless of how many field symbols are packed into
one observation.

For characteristic two and an alphabet of at least four symbols, the only cost
occurs at the exact two-observation saturation point `n=2r`.  The obstruction is
combinatorial: a two-position window pairs every state with its translate, so only
unordered pairs of distinct colours are available.

The binary alphabet is the boundary case where the lack of a second output bit
creates the additional four-dimensional exception.
