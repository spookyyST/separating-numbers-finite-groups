# Separating numbers for elementary abelian groups with field-sized alphabet

This note records a complete classification for the additive groups

\[
V_d=(\mathbb F_q,+)^d
\]

when the observation alphabet also has size `q`, where `q` is a prime power.
No claim of literature priority is made here.

## Theorem

Let `q` be a prime power and `d>=1`.

### Odd characteristic

If `q` is odd, then

\[
\operatorname{sep}_q(V_d)=d
\]

for every `d`.

### Characteristic two, non-binary alphabet

If `q=2^r` with `r>=2`, then

\[
\operatorname{sep}_q(V_d)=
\begin{cases}
3,&d=2,\\
d,&d\ne2.
\end{cases}
\]

### Binary alphabet

For `q=2`, the previously established binary classification is

\[
\operatorname{sep}_2(V_d)=
\begin{cases}
3,&d=2,\\
5,&d=4,\\
d,&\text{otherwise}.
\end{cases}
\]

Thus among field-sized alphabets larger than two, the only exceptional dimension
is `d=2` in characteristic two.

## 1. Counting lower bound

Since `|V_d|=q^d`, any `q`-ary separating window has at least `d` positions:

\[
\operatorname{sep}_q(V_d)\ge d.
\]

## 2. Odd characteristic: a one-line quadratic construction

Assume `q` is odd.  Define

\[
f(x_1,\ldots,x_d)=x_1+x_2^2+\cdots+x_d^2
\]

and take

\[
Y=\{0,e_2,\ldots,e_d\}.
\]

For `i>=2`,

\[
f(x+e_i)-f(x)=2x_i+1.
\]

Because `2` is invertible in `F_q`, these differences recover
`x_2,...,x_d`.  The base value `f(x)` then recovers `x_1`.
The window has exactly `d` positions, so the counting lower bound is attained.

## 3. Odd dimensions over every finite field

For every prime power `q` and every odd dimension `d=2m+1`, define

\[
f(x)=x_1+x_2x_3+x_4x_5+\cdots+x_{2m}x_{2m+1}
\]

and use

\[
Y=\{0,e_2,e_3,\ldots,e_{2m+1}\}.
\]

Then

\[
f(x+e_{2j})-f(x)=x_{2j+1},
\qquad
f(x+e_{2j+1})-f(x)=x_{2j}.
\]

Hence all coordinates except `x_1` are recovered from the translated differences,
and the base value recovers `x_1`.  Therefore

\[
\operatorname{sep}_q(V_d)=d
\]

for every odd `d`, in every characteristic.

## 4. A two-dimensional lifting lemma

Suppose `f:G -> F_q` and a window `Y` containing the identity separate a finite
group `G`.  On

\[
G\times (\mathbb F_q,+)^2
\]

define

\[
F(g,a,b)=f(g)+ab.
\]

Use the embedded old window together with the two new coordinate shifts.
The two new differences are

\[
F(g,a+1,b)-F(g,a,b)=b,
\]

\[
F(g,a,b+1)-F(g,a,b)=a.
\]

Thus `a,b` are recovered first, after which the old `f`-observations recover `g`.
Consequently

\[
\operatorname{sep}_q(G\times\mathbb F_q^2)
\le
\operatorname{sep}_q(G)+2.
\]

When the old construction attains the counting lower bound, the lifted construction
does too.

## 5. The characteristic-two obstruction in dimension two

Let `q` be even and suppose a two-position separating window existed on
`V_2=F_q^2`.  Normalize the window to

\[
Y=\{0,y\},\qquad y\ne0.
\]

Because the additive group has exponent two,

\[
y+y=0.
\]

The two-symbol word at `x+y` is obtained from the word at `x` by swapping its two
coordinates.  A separating map from the `q^2` group elements into the `q^2`
possible two-symbol words would have to be a bijection.  It would therefore use a
diagonal word `(a,a)`.  But such a word is fixed by the coordinate swap, so `x`
and `x+y` would have the same observation word.  This is a contradiction.

Hence

\[
\operatorname{sep}_q(V_2)>2.
\]

The matching three-position upper bound is explicit:

\[
f(a,b)=ab,
\qquad
Y=\{0,e_1,e_2\}.
\]

The two translated differences recover `b` and `a`, respectively.  Therefore

\[
\operatorname{sep}_q(V_2)=3
\]

for every even prime power `q`.

## 6. A four-dimensional seed for every `q=2^r`, `r>=2`

The remaining task for non-binary even `q` is dimension four.  We give a uniform
construction using only the additive-vector-space structure.

Identify the `q` colours with `F_2^r` and the additive group `F_q^4` with
`F_2^{4r}`.  Write a state as

\[
(p,z),
\qquad
p\in F_2^r,
\qquad
z\in F_2^{3r}.
\]

Inside `z`, distinguish three bits `a,b,c`.  There are `3r` derivative slots,
indexed by a direction `a,b,c` and an output bit `1,...,r`.  Reserve the three
slots

\[
(a,1),\quad(b,1),\quad(a,2).
\]

Associate one distinct remaining `z`-bit `w_{i,k}` with every other derivative
slot `(i,k)`.  There are exactly `3r-3` such bits, so together with `a,b,c` this
uses all `3r` bits of `z`.

Define an `r`-bit quadratic map `Q(z)` as follows:

* output bit 1 contains the term `ab`;
* output bit 2 contains the term `ac`;
* for every nonreserved slot `(i,k)`, output bit `k` contains the term
  `i w_{i,k}`.

Finally set

\[
f(p,z)=p+Q(z)
\]

with bitwise addition in `F_2^r`, and use the four-position window consisting of
zero and the three shifts of `a,b,c`.

The three translated differences have `3r` output bits.  Three of them are

\[
b,\qquad a,\qquad c.
\]

Every other derivative bit is its own unique `w_{i,k}`, except that one may also
contain the already recovered bit `a`.  Hence all `3r` bits of `z` are recovered.
The base colour then gives

\[
p=f(p,z)-Q(z).
\]

Thus the four observations recover all `4r` state bits, proving

\[
\operatorname{sep}_{2^r}(F_{2^r}^4)=4
\]

for every `r>=2`.

For example, when `r=2`, one may write

\[
Q_1=ab+c w_2,
\qquad
Q_2=ac+b w_1+c w_3.
\]

The three differences recover, in order, the six bits

\[
b,\ c,\ a,\ w_1,\ w_2,\ a+w_3,
\]

so the state is recovered immediately.

## 7. Completion of the even-characteristic classification

For `q=2^r`, `r>=2`:

* dimension 1 is trivial;
* dimension 2 has exact value 3 by the swap obstruction;
* every odd dimension attains the lower bound by Section 3;
* dimension 4 attains the lower bound by Section 6;
* every larger even dimension follows from repeated two-dimensional lifting.

This proves the stated classification.

## 8. Why `q=2` is different

The four-dimensional seed in Section 6 needs at least two output bits, equivalently
at least four colours.  When `q=2`, there is only one output bit, and the construction
cannot supply three independent internal derivative directions.  The binary case
indeed has the additional exceptional value

\[
\operatorname{sep}_2(F_2^4)=5.
\]

This isolates the binary alphabet as a genuinely more rigid boundary case rather
than treating the `d=4` exception as an isolated computational accident.
