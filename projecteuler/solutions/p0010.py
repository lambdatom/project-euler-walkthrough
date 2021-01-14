def naive():
    p_limit = 2000000
    # p_limit = 10
    p_sum = 2
    primes = [2]
    i = 3
    while i < p_limit:
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
            p_sum += i

        i += 2  # Only check odd numbers

    return p_sum


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())
