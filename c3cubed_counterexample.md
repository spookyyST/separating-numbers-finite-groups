# A counterexample to the proposed universal binary hypothesis

Let \(G=(C_3)^3\), so \(|G|=27\).  Then

\[
\boxed{\operatorname{sep}_2((C_3)^3)=6.}
\]

The information bound is \(\lceil\log_2 27\rceil=5\), so this gives
\(\delta_2((C_3)^3)=1\).  Thus the conjecture that the only positive-defect
groups are \((C_2)^2\) and \((C_2)^4\) is false.

## Reproducible computational proof

It is enough to consider a five-element window containing the identity: any
window can be translated to this form.  There are
\(\binom{26}{4}=14,950\) such normalized windows.

The standard coordinate swaps, nonzero coordinate scalings, and elementary
transvections are automorphisms of \(\mathbb F_3^3\).  The script
`classify_c3cubed_windows.py` uses these automorphisms to split all 14,950
windows into 10 orbits.  For each representative it builds an exact SAT
encoding of the statement that a Boolean function \(f:G\to\{0,1\}\) makes
the five translated values distinguish all 27 group elements.  All ten SAT
instances are UNSAT.

Therefore no separating window of size 5 exists.

The file `c3xc3xc3_size6_certificate.json` contains a size-six certificate
found by the same SAT program and checked directly by evaluating all 27
translated words.  Hence \(\operatorname{sep}_2(G)\le6\), while the UNSAT
classification gives \(\operatorname{sep}_2(G)>5\), proving equality.

## Consequence

The binary lower bound is not universally attained.  Any revised conjecture
must include at least \((C_3)^3\) as a third exceptional group.
