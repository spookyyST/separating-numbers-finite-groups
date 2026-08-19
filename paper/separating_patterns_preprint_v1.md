# Separating Patterns in Finite Groups: Exact Families and a Small Counterexample

**Igor Tomilson**  
Independent researcher

## Abstract

Let \(G\) be a finite group, let \(q\ge 2\), and let \(f:G\to[q]\). For a finite set
\(Y\subseteq G\), consider the translated observation map
\[
\Phi_{f,Y}(x)=(f(xy))_{y\in Y}.
\]
The separating number \(\operatorname{sep}_q(G)\) is the minimum size of \(Y\) for
which \(\Phi_{f,Y}\) is injective for some \(f\).

This note records two exact infinite families and two finite computational results.
First, for every cyclic group \(C_N\),
\[
\operatorname{sep}_q(C_N)=\lceil \log_q N\rceil.
\]
Second, for the elementary abelian binary groups \(V_d=(C_2)^d\),
\[
\operatorname{sep}_2(V_d)=
\begin{cases}
3,&d=2,\\
5,&d=4,\\
d,&\text{otherwise}.
\end{cases}
\]
We also give the exact computational result
\[
\operatorname{sep}_2((C_3)^3)=6>
\lceil\log_2 27\rceil=5,
\]
and explicit certificates showing that every one of the 51 groups of order \(32\)
satisfies
\[
\operatorname{sep}_2(G)=5.
\]

All computational results are accompanied by reproducible scripts and certificates.

## 1. Introduction

Kang and Hsieh introduced a separating-pattern parameter for finite groups in their
study of information and locality in Cayley graphs.

Let \(G\) be a finite group and let \(f:G\to[q]\). For an ordered finite set
\[
Y=(y_1,\ldots,y_t)\subseteq G
\]
define
\[
\Phi_{f,Y}(x)=
\bigl(f(xy_1),\ldots,f(xy_t)\bigr).
\]
We call \((f,Y)\) separating if \(\Phi_{f,Y}\) is injective, and define
\[
\operatorname{sep}_q(G)=
\min\{|Y|:\exists f:G\to[q]\text{ such that }(f,Y)\text{ is separating}\}.
\]

A counting argument gives
\[
\operatorname{sep}_q(G)\ge
\left\lceil\log_q|G|\right\rceil.
\]

The reproducibility package is available at:

`https://github.com/spookyyST/separating-numbers-finite-groups`

## 2. Cyclic groups

### Theorem 2.1

For every \(q\ge2\) and \(N\ge2\),
\[
\boxed{
\operatorname{sep}_q(C_N)=\lceil\log_qN\rceil.
}
\]

### Proof

Let
\[
r=\lceil\log_qN\rceil.
\]
The counting bound gives
\[
\operatorname{sep}_q(C_N)\ge r.
\]

Write \(C_N=\langle s\rangle\). Since \(N\le q^r\), choose a cyclic \(q\)-ary word
\[
c=(c_0,c_1,\ldots,c_{N-1})
\]
of length \(N\) whose cyclic factors of length \(r\) are pairwise distinct.
Such arbitrary-length cut-down de Bruijn sequences exist whenever \(N\le q^r\).

Define
\[
f(s^i)=c_i
\]
and take
\[
Y=(1,s,s^2,\ldots,s^{r-1}).
\]
Then
\[
\Phi_{f,Y}(s^i)
=
(c_i,c_{i+1},\ldots,c_{i+r-1}),
\]
with indices modulo \(N\). These \(N\) words are pairwise distinct, so
\[
\operatorname{sep}_q(C_N)\le r.
\]
Together with the lower bound,
\[
\operatorname{sep}_q(C_N)=r.
\]
\(\square\)

### Remark 2.2

Every cyclic group attains the information lower bound for every alphabet size
\(q\ge2\).

## 3. Elementary abelian binary groups

Let
\[
V_d=\mathbb F_2^d.
\]

### Theorem 3.1

For every \(d\ge1\),
\[
\boxed{
\operatorname{sep}_2(V_d)=
\begin{cases}
3,&d=2,\\
5,&d=4,\\
d,&\text{otherwise}.
\end{cases}
}
\]

Since \(|V_d|=2^d\),
\[
\operatorname{sep}_2(V_d)\ge d.
\]

### 3.1 Odd dimensions

Let \(d=2m+1\). Define
\[
f(x)=x_1+\sum_{j=1}^{m}x_{2j}x_{2j+1}
\]
and take
\[
Y=(0,e_2,e_3,\ldots,e_{2m+1}).
\]

For every \(j\),
\[
f(x+e_{2j})+f(x)=x_{2j+1},
\]
and
\[
f(x+e_{2j+1})+f(x)=x_{2j}.
\]
Thus the observation word recovers \(x_2,\ldots,x_{2m+1}\), and then
\[
x_1
=
f(x)+\sum_{j=1}^{m}x_{2j}x_{2j+1}.
\]
Hence
\[
\operatorname{sep}_2(V_d)=d
\]
for every odd \(d\).

### 3.2 Two-dimensional lifting lemma

### Lemma 3.2

Suppose \((f,Y)\) separates \(V_d\), with
\[
|Y|=d,\qquad 0\in Y.
\]
Then
\[
\operatorname{sep}_2(V_{d+2})=d+2.
\]

### Proof

Write
\[
V_{d+2}=V_d\times\mathbb F_2^2
\]
with new coordinates \(a,b\). Define
\[
F(x,a,b)=f(x)+ab.
\]
Take
\[
Y'
=
\{(y,0,0):y\in Y\}
\cup
\{(0,1,0),(0,0,1)\}.
\]

The new observations determine
\[
F(x,a+1,b)+F(x,a,b)=b,
\]
and
\[
F(x,a,b+1)+F(x,a,b)=a.
\]
Thus \(a,b\) are recovered. After subtracting the known term \(ab\) from the
embedded old observations, one recovers the original \(Y\)-word, hence \(x\).

Therefore \(Y'\) separates \(V_{d+2}\). The counting bound gives equality.
\(\square\)

### 3.3 Dimension six

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
x\longmapsto
\bigl(f(x),f(x+e_1),\ldots,f(x+e_5)\bigr)
\]
is a permutation of \(\mathbb F_2^6\). Hence
\[
\operatorname{sep}_2(V_6)=6.
\]
The lifting lemma gives
\[
\operatorname{sep}_2(V_{2m})=2m
\]
for every \(m\ge3\).

### 3.4 Exceptional dimensions

Finite exhaustive verification gives
\[
\operatorname{sep}_2(V_2)=3,
\qquad
\operatorname{sep}_2(V_4)=5.
\]

For \(d=2\), every normalized two-point pattern is equivalent to
\[
(0,e_1).
\]

For \(d=4\), every normalized four-point pattern is affine-equivalent to one of
two types:
\[
(0,e_1,e_2,e_1+e_2)
\]
or
\[
(0,e_1,e_2,e_3).
\]
The verifier exhaustively checks the corresponding Boolean functions and finds no
separating window of size \(d\). Matching upper bounds are also verified.

This completes the proof of Theorem 3.1.

## 4. A binary counterexample in \((C_3)^3\)

### Theorem 4.1

For
\[
G=(C_3)^3\cong\mathbb F_3^3,
\]
\[
\boxed{
\operatorname{sep}_2(G)=6.
}
\]

Since
\[
\lceil\log_2|G|\rceil
=
\lceil\log_2 27\rceil
=
5,
\]
this group does not attain the information lower bound.

### Computational proof

Any five-element window can be translated so that it contains the identity. It is
therefore enough to consider
\[
\binom{26}{4}=14,950
\]
normalized five-windows.

The group \(GL(3,3)\) acts on these windows. The supplied program generates this
action using coordinate swaps, nonzero coordinate scalings, and elementary
transvections. The 14,950 windows split into ten orbits.

For a fixed representative \(Y\), introduce one Boolean variable \(X_z\) for each
\(z\in G\). For every pair \(g\ne h\), separation requires
\[
\bigvee_{y\in Y}
\bigl(X_{g+y}\operatorname{xor}X_{h+y}\bigr).
\]
The program converts these conditions to CNF with auxiliary XOR variables and
solves every orbit representative exactly. All ten instances are UNSAT.

Thus no separating binary window of size \(5\) exists.

The file `c3xc3xc3_size6_certificate.json` contains an explicit six-element window
and Boolean colouring. A direct verifier checks that its 27 translated words are
pairwise distinct. Therefore
\[
\operatorname{sep}_2((C_3)^3)=6.
\]
\(\square\)

## 5. Groups of order 32

There are 51 groups of order \(32\) in the GAP SmallGroups library.

### Proposition 5.1

For every group \(G\) of order \(32\),
\[
\boxed{
\operatorname{sep}_2(G)=5.
}
\]

### Proof

The counting bound gives
\[
\operatorname{sep}_2(G)\ge5.
\]

For each group
\[
\operatorname{SmallGroup}(32,i),
\qquad 1\le i\le51,
\]
the repository stores an explicit five-element window and a Boolean colouring.

The verification script reconstructs the multiplication table of each group in GAP
and checks directly that the 32 translated words are pairwise distinct. Hence
\[
\operatorname{sep}_2(G)\le5.
\]
Equality follows.
\(\square\)

## 6. Reproducibility

The repository contains:

- `verify_f2_6.py`, for the finite cases \(d=2,4,6\);
- `classify_c3cubed_windows.py`, for the \(GL(3,3)\)-orbit reduction and SAT test;
- `c3xc3xc3_size6_certificate.json`, for the size-six upper bound;
- `order32_sep_certificates.json`, for all 51 groups of order 32;
- `verify_order32_certificates.py`, an independent checker using GAP;
- `search_abelian_examples.py`, a generic SAT search tool.

The generic search tool treats an exhausted bounded search as inconclusive rather
than as a proof of nonexistence.

The principal computational results were independently reproduced by Ming-Hsuan Kang.

## 7. Open problems

1. Determine
   \[
   \operatorname{sep}_2((C_3)^4).
   \]

2. Determine
   \[
   \operatorname{sep}_2((C_5)^3).
   \]

3. Classify finite groups \(G\) satisfying
   \[
   \operatorname{sep}_2(G)
   =
   \lceil\log_2|G|\rceil.
   \]

4. Determine how large the defect
   \[
   \delta_q(G)
   =
   \operatorname{sep}_q(G)
   -
   \lceil\log_q|G|\rceil
   \]
   can be.

5. Find structural conditions forcing
   \[
   \delta_q(G)=0.
   \]

The example \((C_3)^3\) shows that universal equality with the information lower
bound is false, while the order-32 computation shows that noncommutativity alone
does not force positive defect.

## Acknowledgments

I thank Ming-Hsuan Kang and Yu-Hsuan Hsieh for helpful correspondence concerning
their separating-pattern parameter. I also thank Ming-Hsuan Kang for independently
reproducing the main computational results in the accompanying package.

## References

1. M.-H. Kang and Y.-H. Hsieh, *Information and Locality in Cayley Graphs*,
   arXiv:2608.04608v1, 2026.

2. B. Cameron, A. Gündoğan, and J. Sawada, *Cut-Down de Bruijn Sequences*,
   arXiv:2205.02815, 2022.
