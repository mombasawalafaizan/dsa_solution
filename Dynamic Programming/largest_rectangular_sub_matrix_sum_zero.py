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


def sumZeroMatrix(a, r, c):
    """The main function that finds Largest Rectangle
        sub-matrix in matrix arr who sum is 0 """
    fup, fdown, fleft, fright = 0, 0, 0, 0
    max_len = -1
    up = [0]
    down = [0]
    # Setting left column
    for left in range(c):
        temp = [0] * r
        up[0] = -1
        down[0] = -1
        # Setting right column
        for right in range(left, c):
            # Set the right column for the left column
            # set by outer loop
            for i in range(r):
                temp[i] += a[i][right]

            # Find largest subarray with 0 sum in
            # temp[]. The sumZero() function also
            # sets values of start and finish(up and down). So
            # 'sum' is sum of rectangle between (up,
            # left) and (down, right) which is
            # boundary columns strictly as left and right.
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

a = [ [ 9, 7, 16, 5 ], 
    [ 1, -6, -7, 3 ],
        [ 1, 8, 7, 9 ],
         [ 7, -2, 0, 10 ] ]

sumZeroMatrix(a, len(a), len(a[0]))