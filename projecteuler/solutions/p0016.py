def naive():
    pwr = 1000
    digits = str(2**pwr)
    s = 0
    for i in digits:
        s += int(i)

    return s


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())
