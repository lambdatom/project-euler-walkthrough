def collatz(n: int):
    """Return the next number in the Collatz sequence."""
    even = n/2
    if even.is_integer():
        return int(even)
    else:
        return 3*n + 1


def collatz_tree_append(n: int, cs: dict):
    """Append to dict cs all new values of the collatz sequence starting at n."""
    while True:
        next_seq = cs.get(n)
        next_collatz = collatz(n)
        if next_seq is None:
            cs[n] = next_collatz
            n = next_collatz
        else:
            # print(next_collatz)
            assert next_seq == next_collatz, Exception("Next collatz does not match sequence value.")
            break
    return cs


def collatz_seq_length(n, cs):
    length = 1
    while n != 1:
        n = cs[n]
        length += 1

    return length


def get_longest_collatz_seq(n, ct):
    longest_len = 1
    longest_seq = 1

    # We could compute sequence lengths at the same time as the sequences to further optimize.
    for i in range(n, 1, -1):
        clen = collatz_seq_length(i, ct)
        if clen > longest_len:
            longest_seq = i
            longest_len = clen

    print(longest_seq, longest_len)
    return longest_seq


def build_collatz_tree(n):
    """Build the tree of collatz sequence values from 1 to n."""

    collatz_tree = {1: 4}

    for i in range(1, n):
        collatz_tree = collatz_tree_append(i, collatz_tree)

    return collatz_tree


def naive():
    n = 1000000
    ct = build_collatz_tree(n)
    longest_seq = get_longest_collatz_seq(n, ct)

    return longest_seq


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())
