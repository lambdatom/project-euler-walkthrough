# Enumerate each prime up to the n-th
def naive():
    n = 10001
    primes = [2]
    i = 1
    while len(primes) < n:
        i += 2  # Only check odd numbers
        i_sqrt = i**0.5
        is_prime = True

        for p in primes:  # We know all previous primes, use them
            if p > i_sqrt:  # Only check factors up to sqrt(i)
                break
            if i % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    return primes[n-1]


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())
