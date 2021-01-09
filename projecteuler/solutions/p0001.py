def solve():

    s3 = sum(3*i for i in range(1000) if (3*i < 1000))
    s5 = sum(5*i for i in range(1000) if (5*i < 1000 and 5*i % 3 != 0))  # Skip values already counted by 3*i
    s = s3 + s5

    print(s)


if __name__ == "__main__":
    solve()
