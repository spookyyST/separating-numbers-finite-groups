# Separating patterns on additive finite-field vector spaces

Let \(q\) be a prime power and

\[
V_d=(\mathbb F_q,+)^d.
\]

The alphabet is identified with \(\mathbb F_q\), so the parameter is \(\operatorname{sep}_q(V_d)\).
The information lower bound is

\[
\operatorname{sep}_q(V_d)\ge d,
\]

because \(|V_d|=q^d\).

## Theorem 1: odd characteristic

If \(q\) is odd, then for every \(d\ge1\),

\[
\boxed{\operatorname{sep}_q(V_d)=d.}
\]

### Proof

Write \(x=(x_1,\ldots,x_d)\) and define

\[
f(x)=x_1+\sum_{i=2}^d x_i^2.
\]

Take

\[
Y=(0,e_2,\ldots,e_d).
\]

For each \(i\ge2\),

\[
f(x+e_i)-f(x)=(x_i+1)^2-x_i^2=2x_i+1.
\]

Since \(q\) is odd, \(2\ne0\) and this determines \(x_i\). After recovering \(x_2,\ldots,x_d\), the base value \(f(x)\) determines \(x_1\). Thus \(d\) observations separate all \(q^d\) points, and the counting lower bound gives equality. \(\square\)

## Theorem 2: all odd dimensions

For every prime power \(q\) and every odd \(d=2m+1\),

\[
\boxed{\operatorname{sep}_q(V_d)=d.}
\]

### Proof

Define

\[
f(x)=x_1+\sum_{j=1}^{m}x_{2j}x_{2j+1}
\]

and take

\[
Y=(0,e_2,e_3,\ldots,e_d).
\]

For each \(j\),

\[
f(x+e_{2j})-f(x)=x_{2j+1},
\]

and

\[
f(x+e_{2j+1})-f(x)=x_{2j}.
\]

Hence the shifted observations recover \(x_2,\ldots,x_d\), after which the base value recovers \(x_1\). The counting lower bound again gives equality. \(\square\)

## Theorem 3: two-coordinate lifting

Let \(G\) be any finite group. Suppose a \(q\)-ary separating pair \((f,Y)\) for \(G\) has size \(t\), and normalize it so that the identity lies in \(Y\). Then

\[
\boxed{
\operatorname{sep}_q\bigl(G\times(\mathbb F_q,+)^2\bigr)
\le
\operatorname{sep}_q(G)+2.
}
\]

### Proof

Define

\[
F(g,a,b)=f(g)+ab.
\]

Use the embedded old window together with the two new coordinate shifts:

\[
Y'=
\{(y,0,0):y\in Y\}
\cup
\{(1_G,1,0),(1_G,0,1)\}.
\]

The observation at the identity is \(F(g,a,b)\). Therefore

\[
F(g,a+1,b)-F(g,a,b)=b,
\]

and

\[
F(g,a,b+1)-F(g,a,b)=a.
\]

The two new coordinates recover \(a,b\). Subtracting the known term \(ab\) from the embedded old observations recovers the original \(Y\)-word of \(f\), hence \(g\). \(\square\)

## Theorem 4: one-coordinate lifting in odd characteristic

If \(q\) is odd, then under the same hypotheses,

\[
\boxed{
\operatorname{sep}_q\bigl(G\times(\mathbb F_q,+)\bigr)
\le
\operatorname{sep}_q(G)+1.
}
\]

Define

\[
F(g,a)=f(g)+a^2
\]

and add the single shift \((1_G,1)\). The difference from the identity coordinate is

\[
(a+1)^2-a^2=2a+1,
\]

which determines \(a\) because \(2\ne0\). The old word then recovers \(g\).

## Corollary 5: defect monotonicity

Define

\[
\delta_q(G)=\operatorname{sep}_q(G)-\lceil\log_q|G|\rceil.
\]

Since multiplying the group order by \(q^r\) increases the counting lower bound by exactly \(r\), Theorems 3 and 4 imply:

- for every prime power \(q\), adjoining two additive \(\mathbb F_q\)-coordinates does not increase \(\delta_q\);
- for odd \(q\), adjoining one additive \(\mathbb F_q\)-coordinate does not increase \(\delta_q\).

## Theorem 6: a characteristic-2 obstruction in dimension two

If \(q\) is even, then

\[
\boxed{\operatorname{sep}_q(V_2)=3.}
\]

### Lower bound beyond counting

The counting bound only gives 2. Suppose a two-element window separated \(V_2\). After normalization it has the form

\[
Y=(0,y),\qquad y\ne0.
\]

Because the additive group has characteristic 2,

\[
y+y=0.
\]

Thus if the word at \(x\) is

\[
(f(x),f(x+y)),
\]

then the word at \(x+y\) is the swapped pair

\[
(f(x+y),f(x)).
\]

Since there are exactly \(q^2\) states and exactly \(q^2\) two-letter \(q\)-ary words, injectivity would force the observation map to be a bijection onto the whole square \(\mathbb F_q^2\). In particular some diagonal word \((a,a)\) would occur. But then \(x\) and \(x+y\) would have the same word, contradicting injectivity. Hence no two-element window exists.

### Upper bound

For \(x=(a,b)\), define

\[
f(a,b)=ab
\]

and use

\[
Y=(0,e_1,e_2).
\]

Then

\[
f(a+1,b)-f(a,b)=b,
\qquad
f(a,b+1)-f(a,b)=a.
\]

Thus three observations recover both coordinates. Hence \(\operatorname{sep}_q(V_2)=3\). \(\square\)

## Consequence for even \(q\)

Combining the dimension-two seed with the two-coordinate lifting gives, for even \(q\) and even \(d\),

\[
d\le \operatorname{sep}_q(V_d)\le d+1.
\]

For odd \(d\), Theorem 2 gives the exact value \(d\).

The binary case \(q=2\) has additional structure: the accompanying project separately proves the exact formula for all \(d\), including the exceptional dimensions \(2\) and \(4\).

## Status

These arguments are elementary and self-contained. A search of the current Kang--Hsieh preprint did not locate a direct-product or lifting statement of this form. No broader priority claim is made without a dedicated literature review.
