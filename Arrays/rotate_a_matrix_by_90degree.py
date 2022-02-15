def rotateMatrix(matrix, n):
    sub_size = n
    for l in range(n//2):
        for i in range(sub_size-1):
            swap(matrix, l+i, l, n-l-1, l+i)
            swap(matrix, n-l-1, l+i, n-l-1-i, n-l-1)
            swap(matrix, n-l-1-i, n-l-1, l, n-l-1-i)
        sub_size -= 2


def swap(matrix, i1, j1, i2, j2):
    temp = matrix[i2][j2]
    matrix[i2][j2] = matrix[i1][j1]
    matrix[i1][j1] = temp

n = int(input())
matrix = [list(range(i+1, i+1+n)) for i in range(0, n*n, n)]
for j in matrix:
    for i in j:
        print("%2d" % i, end=' ')
    print()
print()
rotateMatrix(matrix, n)
for j in matrix:
    for i in j:
        print("%2d" % i, end=' ')
    print()
print()