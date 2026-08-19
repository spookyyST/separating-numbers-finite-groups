# Near-full binary cube constraints for optimal separating windows

Let \(G\) be a finite group and suppose a binary separating pair \((f,Y)\) has
\(|Y|=t\). Write

\[
\Phi(x)=(f(xy))_{y\in Y}\in\{0,1\}^t.
\]

Assume

\[
|G|=2^t-m,
\]

so the injective image of \(\Phi\) misses exactly \(m\) binary words.
Let

\[
A=f^{-1}(1),\qquad w=|A|,
\]

and let \(M\subseteq\{0,1\}^t\) be the set of missing words.

## Lemma 1: equal missing-column weights

Every coordinate of the \(m\times t\) matrix formed by the missing words has the same number

\[
r=2^{t-1}-w
\]

of ones.

### Proof

Fix \(y\in Y\). Since right multiplication by \(y\) is a bijection of \(G\), the number of \(x\in G\) for which \(f(xy)=1\) is exactly \(|A|=w\). Thus every coordinate of the image \(\Phi(G)\) contains exactly \(w\) ones.

The complete cube \(\{0,1\}^t\) contains \(2^{t-1}\) ones in every coordinate. Therefore the missing set contains exactly

\[
2^{t-1}-w
\]

ones in every coordinate. \(\square\)

Complementing \(f\) replaces \(r\) by \(m-r\). If \(m>1\), the cases \(r=0\) and \(r=m\) are impossible because all missing words would then be identical. Hence

\[
1\le r\le m-1.
\]

## Corollary 2: one, two, and three missing words

If \(m=1\), the unique missing word is either \(0^t\) or \(1^t\).

If \(m=2\), the two missing words are complements of each other.

If \(m=3\), after complementing \(f\) if necessary, one may assume \(r=1\). Then every coordinate belongs to the support of exactly one of the three missing words. Thus their supports form a partition

\[
[t]=B_1\sqcup B_2\sqcup B_3,
\]

where at most one block may be empty.

## Lemma 3: intersection numbers from the missing words

For coordinates \(i_1,\ldots,i_s\), the number of \(x\in G\) for which all selected observations equal one is

\[
2^{t-s}-N_M(i_1,\ldots,i_s),
\]

where \(N_M(i_1,\ldots,i_s)\) is the number of missing words having a one in every selected coordinate.

This follows by subtracting the missing rows from the complete binary cube.

## Application to \((C_5)^3\)

For \(G=(C_5)^3\),

\[
|G|=125=2^7-3.
\]

Therefore an optimal binary separator of size seven, if it exists, must satisfy the \(m=3\) case above. After complementing \(f\), we may assume

\[
|A|=63.
\]

The three missing seven-bit words have pairwise disjoint supports that partition the seven coordinates.

For two window positions \(y_i,y_j\), let

\[
c(y_j-y_i)=|A\cap(A+(y_i-y_j))|.
\]

The complete seven-cube has 32 words with ones in both coordinates. Hence

\[
c(y_j-y_i)=
\begin{cases}
31,& i,j\text{ lie in the same missing-support block},\\
32,& i,j\text{ lie in different blocks}.
\end{cases}
\]

Thus the graph on the seven window positions whose edges are the pairs with autocorrelation 31 must be a disjoint union of at most three cliques.

This is a necessary condition for

\[
\operatorname{sep}_2((C_5)^3)=7.
\]

It does not by itself prove existence or nonexistence, but it substantially narrows the structure of any optimal certificate and gives a stronger target for future SAT or combinatorial searches.
