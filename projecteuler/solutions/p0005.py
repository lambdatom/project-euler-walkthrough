# Just test multiples of 20 mod each
# Ignore skipping redundant factors such as 2,5,10
def naive():
    ni = 20
    n = ni
    while True:
        for i in range(1, ni+1):
            if n % i != 0:
                break
            elif i < ni:
                continue
            else:
                return n
        n = n + ni


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())
