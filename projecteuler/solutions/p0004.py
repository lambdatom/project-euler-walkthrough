# Return true if n is palindromic
def is_palindromic(n):
    n_str = str(n)
    return n_str == n_str[::-1]


def get_largest_ndigit_factor(n, d):
    lower_d = int(''.ljust(d-1, '9'))
    upper_d = int(''.ljust(d, '9'))
    for factor in range(n-1, 1, -1):
        if factor > upper_d:
            continue
        elif factor <= lower_d:
            return 1
        elif n % factor == 0:
            factor2 = int(n / factor)
            if len(str(factor2)) == d:
                return factor


# The largest product of two 3-digit numbers would be the product of 999 * 999
def naive():
    n1 = 999
    m = n1 * n1
    palindromes = []

    for i in range(m, 0, -1):
        if is_palindromic(i):
            palindromes.append(i)

    for i in palindromes:
        f = get_largest_ndigit_factor(i, len(str(n1)))
        if f != 1:
            return i

    return 1


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())
