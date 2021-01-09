def get_smallest_factor(n):
    assert n >= 2
    for factor in range(2, n):
        if factor > n/2:
            return n
        if n % factor == 0:
            return factor


# Get the prime factors of n
def get_factors(n):
    factors = []
    prime_factor = get_smallest_factor(n)
    factors.append(prime_factor)

    while prime_factor < n:
        n = int(n / prime_factor)
        print(prime_factor, n)
        prime_factor = get_smallest_factor(n)
        factors.append(prime_factor)

    return factors


def solve():
    return max(get_factors(600851475143))


if __name__ == "__main__":
    print(solve())
