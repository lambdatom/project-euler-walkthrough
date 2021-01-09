from common import fibonacci

fib_max_value = 4000000


# Naive brute force approach, re-calculating the Fibonacci sequence on each iteration.
def naive():
    s = 0
    for n in range(0, fib_max_value):
        # Get the
        m = fibonacci(n)
        if m > fib_max_value:
            break
        if m % 2 == 0:
            s += m
    return s


# This approach instead iterates through the Fibonacci sequence while checking and summing.
def fibonacci_upto_max(max_value):

    fn2 = 0  # Fib(n-2)
    fn1 = 1  # Fib(n-1)
    fn = 0

    s = 0

    # Since F(n) grows faster than n, F(n) >= n. We can use n as an upper bound for iteration then.
    for i in range(1, max_value):
        if fn > max_value:
            break
        if fn % 2 == 0:
            s += fn
        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn

    return s


def attempt():
    print(naive())
    print(fibonacci_upto_max(fib_max_value))


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())

