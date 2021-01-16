import math
import itertools


def is_positive_integer(n):
    """Return whether n is a positive integer."""
    return n > 0 and isinstance(n, int)


def fibonacci(n: int):
    """
    Return the nth Fibonacci number.

    See: https://mathworld.wolfram.com/FibonacciNumber.html
    """
    assert is_positive_integer(n)

    if n == 0:
        return 0
    else:
        fn2 = 0  # Fib(n-2)
        fn1 = 1  # Fib(n-1)
        fn = 1

        for i in range(1, n):
            fn = fn1 + fn2
            fn2 = fn1
            fn1 = fn

        return fn


def prime_factors(n: int):
    """
    Return the list of all prime factors of n.

    See: https://mathworld.wolfram.com/PrimeFactorization.html
    """
    assert is_positive_integer(n)

    pfs = []
    limit = math.isqrt(n)
    current = n

    i = 2
    while current > 1:

        if current % i == 0:
            pfs.append(i)
            current = int(current / i)
        else:
            if i > 2:
                i += 2
            elif i == 2:
                i += 1

    return pfs


# From Itertools Recipes
# https://docs.python.org/3/library/itertools.html
def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def divisors(n: int):
    """
    Return the list of all divisors of n.

    See: https://mathworld.wolfram.com/Divisor.html
    """
    assert is_positive_integer(n)

    pfs = prime_factors(n)

    pfs_powerset = powerset(pfs)

    pfs_products = []
    for ps in pfs_powerset:
        prod = 1
        for p in ps:
            prod *= p
        pfs_products.append(prod)

    return list(set(pfs_products))
