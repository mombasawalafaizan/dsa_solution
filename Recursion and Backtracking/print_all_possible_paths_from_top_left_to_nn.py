def printPath(mat, i, j, r, c, path, idx):
    if i==r-1 and j==c-1:
        path[idx] = mat[i][j]
        print(path)
        return 
    path[idx] = mat[i][j]
    if i < r-1:
        printPath(mat, i+1, j, r, c, path, idx+1)
    if j < c-1:
        printPath(mat, i, j+1, r, c, path, idx+1)

    

if __name__ == "__main__":
    mat = [[1, 2], [3, 4]]
    r = 2
    c = 2
    path = [0] * (r+c-1)
    printPath(mat, 0, 0, r, c, path, 0)