def maximumSumRectangle(R,C,M):
        #code here
        preSum = [[0 for _ in range(C+1)] for _ in range(R)]
        max_sum = -5 * 10**9
        for i in range(R):
            for j in range(C):
                preSum[i][j+1] = preSum[i][j] + M[i][j]
                
        for left in range(C):
            for right in range(left, C):
                max_ending_here = preSum[0][right+1]-preSum[0][left]
                max_sum = max(max_sum, max_ending_here)
                for row in range(1, R):
                    temp = preSum[row][right+1]-preSum[row][left]
                    max_ending_here = max(max_ending_here + temp, temp)
                    max_sum = max(max_sum, max_ending_here)
        return max_sum