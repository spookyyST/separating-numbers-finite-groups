# Binary separating patterns in finite groups

## Abstract

For the separating-pattern parameter introduced by Kang and Hsieh, we record
two exact families and one exact computational counterexample to naive
attainment of the binary information bound.  First, for every cyclic group
\(C_N\), cut-down de Bruijn words yield
\(\operatorname{sep}_q(C_N)=\lceil\log_qN\rceil\).  Second, for
\(V_d=(C_2)^d\),

\[
\operatorname{sep}_2(V_d)=
\begin{cases}
3,&d=2,\\
5,&d=4,\\
d,&\text{otherwise}.
\end{cases}
\]

Finally, an exact SAT computation gives
\(\operatorname{sep}_2((C_3)^3)=6\), despite the information bound being
five.  The computation reduces all normalized five-windows to ten linear
automorphism orbits and supplies a verified size-six certificate.  We also
provide size-five certificates for every group of order 32.

## 1. Separating patterns

Let \(G\) be a finite group and \(f:G\to[q]\).  A finite set
\(Y\subseteq G\) is separating for \(f\) when

\[
x\longmapsto (f(xy))_{y\in Y}
\]

is injective.  Write \(\operatorname{sep}_q(G)\) for the least possible
size of such a set.  Counting gives the universal lower bound

\[
\operatorname{sep}_q(G)\ge\lceil\log_q|G|\rceil.
\]

## 2. Cyclic groups

For \(r=\lceil\log_qN\rceil\), take a cyclic q-ary word of length \(N\)
whose cyclic length-\(r\) factors are pairwise distinct.  Such cut-down de
Bruijn words exist for every \(N\le q^r\).  Labelling \(s^i\in C_N\) by the
\(i\)-th symbol and taking \(Y=(1,s,\ldots,s^{r-1})\) yields distinct
translated words.  Thus

\[
\operatorname{sep}_q(C_N)=\lceil\log_qN\rceil.
\]

## 3. Elementary abelian binary groups

Let \(V_d=\mathbb F_2^d\).  For \(d=2m+1\), define

\[
f(x)=x_1+\sum_{j=1}^{m}x_{2j}x_{2j+1}
\]

and use \(Y=(0,e_2,e_3,\ldots,e_{2m+1})\).  The differences between the
value at \(0\) and the values at the paired basis directions recover
\(x_2,\ldots,x_{2m+1}\); the remaining coordinate follows from \(f(x)\).
This proves optimality in every odd dimension.

If an optimal pair \((f,Y)\), with \(0\in Y\), exists in dimension \(d\),
then

\[
F(x,a,b)=f(x)+ab
\]

together with the embedded copy of \(Y\) and the two new coordinate vectors
separates \(V_{d+2}\).  The two extra observations recover \(a,b\), after
which the old word is recovered.  A finite checked seed in dimension six
therefore gives every even dimension at least six.  Exhaustive finite checks
give the exceptional values in dimensions two and four.

Hence

\[
\operatorname{sep}_2(V_d)=
\begin{cases}
3,&d=2,\\
5,&d=4,\\
d,&\text{otherwise}.
\end{cases}
\]

## 4. The \((C_3)^3\) counterexample

For \(G=\mathbb F_3^3\), the counting bound is five.  Every separating
five-window can be translated to contain \(0\), leaving \(\binom{26}{4}
=14,950\) normalized windows.  Coordinate permutations, nonzero coordinate
scalings, and elementary transvections reduce them to ten orbits.

For a fixed window \(Y\), introduce Boolean variables \(X_z\), one for each
\(z\in G\).  For each unordered pair \(g\ne h\), require

\[
\bigvee_{y\in Y}(X_{g+y}\mathbin{\operatorname{xor}}X_{h+y}).
\]

The supplied program encodes these conditions in CNF using auxiliary XOR
variables.  All ten orbit representatives are unsatisfiable.  Conversely, a
stored size-six certificate directly produces 27 distinct binary words.
Therefore

\[
\operatorname{sep}_2((C_3)^3)=6.
\]

## 5. Order 32

For each GAP SmallGroup(32,i), \(1\le i\le51\), the package stores a
five-element window and a Boolean colouring which produce 32 distinct words.
The counting bound is five, proving

\[
\operatorname{sep}_2(G)=5\qquad (|G|=32).
\]

## 6. Scope

These results do not provide a classification of all finite groups.  In
particular, the values for \((C_3)^4\) and \((C_5)^3\) are open in this
project.  A literature review is also still needed before making any claim of
priority for the elementary-abelian results.
