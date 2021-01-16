from projecteuler.solutions.common import divisors


def naive():

    i = 1
    s = 0
    divs = []
    while len(divs) < 500:
        s += i
        divs = divisors(s)
        print(s, len(divs), divs)
        i += 1

    return s


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())
