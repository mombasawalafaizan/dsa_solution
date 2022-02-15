def ratInMaze(arr, i, j, path, n, res):
    if arr[i][j] == 0:
        return
    if i == n-1 and j == n-1:
        res.append(path)
        return
    arr[i][j]=0
    if i < n-1 and arr[i+1][j] == 1:
        ratInMaze(arr, i+1, j, path+'D', n, res)
    if j < n-1 and arr[i][j+1] == 1:
        ratInMaze(arr, i, j+1, path+'R', n, res)
    if i > 0 and arr[i-1][j] == 1:
        ratInMaze(arr, i-1, j, path+'U', n, res)
    if j > 0 and arr[i][j-1] == 1:
        ratInMaze(arr, i, j-1, path+'L', n, res)
    arr[i][j]=1
    
def findPath(arr, n):
    # code here
    res = []
    ratInMaze(arr, 0, 0, '', n, res)
    return sorted(res)