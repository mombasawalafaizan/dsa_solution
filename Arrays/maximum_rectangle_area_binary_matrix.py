from collections import deque

def largestAreaUnderHist(arr, m):
    stack = deque()
    # arr.append(0)
    i = 0
    max_area = 0
    cur_area = 0
    while i <= m:
        cur_val = arr[i] if i!=m else 0
        if not stack or cur_val > arr[stack[-1]]:
            stack.append(i)
        else:
            while stack and cur_val < arr[stack[-1]]:
                pos = stack.pop()
                if not stack:
                    cur_area = arr[pos] * i
                else:
                    cur_area = arr[pos] * (i - stack[-1] - 1)
                if cur_area > max_area:
                    max_area = cur_area
            stack.append(i)
        i += 1
    
    return max_area
        
    
def maxRectangle(M, n, m):
    if len(M) == 0:
        return 0
    result = largestAreaUnderHist(M[0], m)
    for i in range(1, n):
        for j in range(m):
            if M[i][j] == 1:
                M[i][j] = M[i-1][j] + M[i][j]
        result = max(result, largestAreaUnderHist(M[i], m))
    return result