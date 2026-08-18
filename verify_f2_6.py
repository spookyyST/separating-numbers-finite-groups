"""Direct certificate for sep_2(F_2^6)=6.

Coordinates use the bits of an integer x: bit i is x_{i+1}.
"""


def f(x: int) -> int:
    bits = [(x >> i) & 1 for i in range(6)]
    x1, x2, x3, x4, x5, x6 = bits
    return (
        x2
        ^ (x1 & x2)
        ^ (x1 & x3)
        ^ (x2 & x3)
        ^ (x3 & x4)
        ^ (x2 & x5)
        ^ (x1 & x4 & x5)
        ^ (x3 & x4 & x5)
        ^ x6
        ^ (x2 & x6)
        ^ (x3 & x6)
        ^ (x4 & x6)
        ^ (x1 & x4 & x6)
        ^ (x3 & x4 & x6)
        ^ (x4 & x5 & x6)
    )


window = (0, 1, 2, 4, 8, 16)
observations = {
    tuple(f(x ^ y) for y in window)
    for x in range(64)
}

assert len(observations) == 64


def separates(d: int, pattern: tuple[int, ...], truth_table: int) -> bool:
    words = set()
    for x in range(1 << d):
        word = tuple((truth_table >> (x ^ y)) & 1 for y in pattern)
        if word in words:
            return False
        words.add(word)
    return True


def no_size_d_pattern_in_normal_form(d: int, pattern: tuple[int, ...]) -> bool:
    return not any(
        separates(d, pattern, truth_table)
        for truth_table in range(1 << (1 << d))
    )


# Up to affine automorphism, these are all two-point patterns in F_2^2
# and all four-point patterns in F_2^4, respectively.
assert no_size_d_pattern_in_normal_form(2, (0, 1))
assert no_size_d_pattern_in_normal_form(4, (0, 1, 2, 4))
assert no_size_d_pattern_in_normal_form(4, (0, 1, 2, 3))

print("Verified: sep_2(F_2^2) > 2, sep_2(F_2^4) > 4, sep_2(F_2^6) = 6")
