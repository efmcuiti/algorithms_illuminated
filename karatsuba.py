import math
"""
Created on: November 6, 2019
Author: efmcuiti
"""
def karatsuba(x, y):
    """
    x, y: Positive integers of length "n".

    Returns the multiplication result using karatsuba's technique.
    """
    assert x >= 0 and y >= 0
    sx, sy = str(x), str(y)
    n = len(sx)
    log2 = math.log(n, 2)

    assert (2**log2 == n) or (n is 1)
    assert len(sy) is n

    if n is 1:
        return x * y
    else:
        half = n//2
        a, b = int(sx[:half]), int(sx[half:])
        c, d = int(sy[:half]), int(sy[half:])
        p, q = a + b, c + d
        ac, bd, pq = karatsuba(a, c), karatsuba(b, d), p * q
        adbc = pq - ac - bd
        return (10**n * ac) + (10**(n//2) * adbc) + bd
