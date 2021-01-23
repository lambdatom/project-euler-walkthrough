# Traverse the binary tree in reverse, just sum each back up to the origin
def naive():

    # Construct an appropriate matrix for summing possible traversals
    n = 20
    lattice = [[0 for i in range(n+1)] for j in range(n+1)]

    for i in range(1, n+1):
        lattice[i][0] = 1
        lattice[0][i] = 1

    for i in range(1, n+1):
        for j in range(1, n+1):
            lattice[i][j] = lattice[i-1][j] + lattice[i][j-1]

    return lattice[n][n]


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())
