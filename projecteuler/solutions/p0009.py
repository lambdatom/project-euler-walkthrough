def find_pairs():
    pairs = {}

    a = 1
    a_limit = 500*(2-2**0.5)
    while a < a_limit:
        b = 1000*(500-a)/(1000-a)
        if b.is_integer():
            pairs[a] = b
        a += 1

    return pairs


def math_it():
    ps = find_pairs()
    assert len(ps) == 1  # Ensure our math is correct as only one solution should exist.
    (a, b) = next(iter(ps.items()))
    product = int(a*b*(1000-a-b))

    return product


def solve():
    return math_it()


if __name__ == "__main__":
    print(solve())
