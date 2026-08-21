# Search status for `(C_19)^3`

The information-theoretic lower bound is 13 because `ceil(log2(19^3)) = 13`.

For the coordinate-line window used in the odd-prime rank-3 experiments, attaining 13 is equivalent to finding 361 pairwise vertex-disjoint directed 19-cycles in the binary de Bruijn graph `dB(2,13)`. Equivalently, select 361 binary cyclic words of length 19 whose 19 cyclic factors of length 13 are all globally distinct.

The generated instance contains 27,348 admissible 19-cycles. A local GLP-style maximum-independent-set search has currently found a verified packing of 327 cycles. This is a lower bound for the packing problem only, not yet a separating certificate for all 6,859 group elements.

The workflow `search_p19_kamis.yml` builds the exact conflict graph and runs KaMIS OnlineMIS and ReduMIS. Every reported solver output is rechecked from the underlying cyclic words before it is accepted as a search artifact.
