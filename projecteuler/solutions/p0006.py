# Just compute the value
def naive():
    n = 100
    s = sum_sq = 0
    for i in range(1, n+1):
        s += i
        sum_sq += i**2

    sq_sum = s**2

    return sq_sum - sum_sq


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())
