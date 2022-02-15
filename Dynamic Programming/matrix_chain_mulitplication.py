def optimal_parenthesis(s, i, j):
    if i == j:
        print(chr(65 + i), end="")
    else:
        print("(", end="")
        optimal_parenthesis(s, i, s[i][j] - 1)
        optimal_parenthesis(s, s[i][j], j)
        print(")", end="")


def matrix_chain_order(p: list, n: int):
    m = [[0] * n for i in range(n)]
    s = [[-1] * n for i in range(n)]
    for l in range(1, n + 1):
        for i in range(0, n - l):
            j = i + l
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k + 1
    for i in m:
        for j in i:
            print("{t:5d}".format(t=j), end=" ")
        print()
    print("-------------------")
    for i in s:
        for j in i:
            print("{t:2d}".format(t=j), end=" ")
        print()
    return m, s


if __name__ == "__main__":
    n = int(input("Enter number of matrix to multiply: "))
    print("Enter dimensions:")
    p = [int(input("Enter p" + str(i) + ": ")) for i in range(n + 1)]
    m, s = matrix_chain_order(p, n)
    print("\nCost of matrix:", m[0][n - 1])
    print("Sequence of the matrix:", end=" ")
    optimal_parenthesis(s, 0, n - 1)
