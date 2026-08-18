# Separating patterns for elementary abelian 2-groups

Let \(V_d=\mathbb F_2^d\). The results below use the binary alphabet \(\mathbb F_2\).

## Theorem

For every \(d\geq1\),

\[
\operatorname{sep}_2(V_d)=
\begin{cases}
3,&d=2,\\
5,&d=4,\\
d,&\text{otherwise}.
\end{cases}
\]

The claims for \(d=2,4,6\) use the accompanying finite verification certificate. The infinite parts follow from the explicit constructions and the two-dimensional lifting lemma below.

## Counting lower bound

If a binary separating pattern has \(t\) positions, it gives \(2^d\) distinct binary words of length \(t\). Hence

\[
\operatorname{sep}_2(V_d)\geq d.
\]

## Odd dimensions

Let \(d=2m+1\). Set

\[
f(x)=x_1+\sum_{j=1}^{m}x_{2j}x_{2j+1}
\]

and

\[
Y=(0,e_2,e_3,\ldots,e_{2m+1}).
\]

For every \(j\),

\[
f(x+e_{2j})+f(x)=x_{2j+1},\qquad
f(x+e_{2j+1})+f(x)=x_{2j}.
\]

Thus the observed word recovers \(x_2,\ldots,x_{2m+1}\), and then

\[
x_1=f(x)+\sum_{j=1}^{m}x_{2j}x_{2j+1}.
\]

So \(|Y|=d\) separates \(V_d\). The counting lower bound proves \(\operatorname{sep}_2(V_d)=d\).

## Two-dimensional lifting lemma

Suppose \(f:V_d\to\mathbb F_2\) and an ordered pattern

\[
Y=(0,y_2,\ldots,y_d)
\]

separate \(V_d\). Define a function on \(V_{d+2}=V_d\times\mathbb F_2^2\) by

\[
F(x,a,b)=f(x)+ab
\]

and take

\[
Y'=
\bigl((y,0,0):y\in Y\bigr)
\cup\{(0,1,0),(0,0,1)\}.
\]

This has \(d+2\) positions. Write \(A=F(x,a,b)\) for the coordinate at \((0,0,0)\). The two new coordinates determine

\[
F(x,a+1,b)+A=b,
\qquad
F(x,a,b+1)+A=a.
\]

After recovering \(a,b\), subtracting \(ab\) from the coordinates indexed by \(Y\) recovers the original \(Y\)-word of \(f\), hence \(x\). Therefore \(Y'\) separates \(V_{d+2}\).

Consequently,

\[
\operatorname{sep}_2(V_d)=d
\quad\Longrightarrow\quad
\operatorname{sep}_2(V_{d+2})=d+2.
\]

## The dimension-six seed

For \(V_6\), take

\[
Y=(0,e_1,e_2,e_3,e_4,e_5)
\]

and

\[
\begin{aligned}
f={}&x_2+x_1x_2+x_1x_3+x_2x_3+x_3x_4+x_2x_5\\
&+x_1x_4x_5+x_3x_4x_5+x_6+x_2x_6+x_3x_6+x_4x_6\\
&+x_1x_4x_6+x_3x_4x_6+x_4x_5x_6.
\end{aligned}
\]

The accompanying verifier checks that

\[
x\longmapsto (f(x),f(x+e_1),\ldots,f(x+e_5))
\]

is a permutation of \(\mathbb F_2^6\). Hence \(\operatorname{sep}_2(V_6)=6\). The lifting lemma now proves \(\operatorname{sep}_2(V_{2m})=2m\) for every \(m\geq3\).

## Exceptional dimensions

An exhaustive search gives

\[
\operatorname{sep}_2(V_2)=3,
\qquad
\operatorname{sep}_2(V_4)=5.
\]

For \(d=2\), every two-point pattern is affine-equivalent to \((0,e_1)\). For \(d=4\), every four-point pattern is affine-equivalent to one of two cases: an affine plane \((0,e_1,e_2,e_1+e_2)\), or an affine-independent set \((0,e_1,e_2,e_3)\). Exhaustive evaluation of all Boolean functions in each normal form produces no separating pattern of size \(d\). The quadratic lifting construction gives the matching upper bounds \(3\) and \(5\).

## Scientific status

The proof is complete modulo the finite, directly reproducible checks in dimensions \(2,4,6\). It is a candidate original result; novelty relative to the broader Boolean-functions literature still requires a dedicated literature review.
