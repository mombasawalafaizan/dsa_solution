def sumZero(a, st, fin, r):
    preSum = dict()
    cur_sum = 0
    max_len = 0
    for i in range(r):
        cur_sum += a[i]
        if cur_sum == 0:
            st[0] = 0
            fin[0] = i
            max_len = i+1
        elif cur_sum in preSum:
            if (i - preSum[cur_sum]) > max_len:
                max_len = i - preSum[cur_sum]
                st[0] = preSum[cur_sum] + 1
                fin[0] = i
        else:
            preSum[cur_sum] = i
    return max_len!=0

def equal01SubMatrix(a, r, c):
    fup, fdown, fleft, fright = 0, 0, 0, 0
    up = [-1]
    down = [-1]
    max_len = 0
    for left in range(c):
        temp = [0] * r
        up[0] = -1
        down[0] = -1
        for right in range(left, c):
            for i in range(r):
                temp[i] += (1 if a[i][right] == 1 else -1)
            sum = sumZero(temp, up, down, r)
            ele = (down[0]-up[0]+1)*(right-left+1)

            if sum and ele > max_len:
                fup = up[0]
                fdown = down[0]
                fleft = left
                fright = right
                max_len = ele

    if (fup == 0 and fdown == 0 and fleft == 0 and fright == 0 and a[0][0] != 0):
        print('No zero matrix exists')
        return
    for i in range(fup, fdown+1):
        for j in range(fleft, fright+1):
            print(a[i][j], end=' ')
        print()
    print('Maxlen', max_len)

# mat = [ [0, 0, 1, 1],
#         [0, 1, 1, 0],
#         [1, 1, 1, 0],
#         [1, 0, 0, 1] ]

mat = [ [0, 0, 1, 1],
        [0, 1, 1, 1] ]   
equal01SubMatrix(mat, len(mat), len(mat[0]))