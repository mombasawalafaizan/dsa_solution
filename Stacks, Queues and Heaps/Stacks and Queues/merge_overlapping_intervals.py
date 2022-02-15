from collections import deque

# Using stack
def mergeIntervals(intervals, n):
    sorted_intervals = []
    for i in range(0,2*n,2):
        sorted_intervals.append([intervals[i], intervals[i+1]])
    sorted_intervals.sort()
    stack = deque()
    stack.append(sorted_intervals[0])
    for i in range(1, n):
        top = stack[-1]
        if top[1] < sorted_intervals[i][0]:
            stack.append(sorted_intervals[i])
        elif top[1] < sorted_intervals[i][1]:
            top = stack.pop()
            top[1] = sorted_intervals[i][1]
            stack.append(top)
    ans = [0] * (2*len(stack))
    i = len(stack)-1 
    while stack:
        top = stack.pop()
        ans[2*i] = top[0]
        ans[2*i+1] = top[1]
        i -= 1
    return ans
            
# In O(1) time without using stack
def mergeIntervals1(intervals, n):
    arr = []
    for i in range(0,2*n,2):
        arr.append([intervals[i], intervals[i+1]])
    arr.sort()
    idx = 0
    for i in range(1, n):
        if arr[idx][1] >= arr[i][0]:
            arr[idx][0] = min(arr[idx][0], arr[i][0])
            arr[idx][1] = max(arr[idx][1], arr[i][1])
        else:
            idx += 1
            arr[idx] = arr[i]
    ans = []
    for i in range(idx+1):
        ans.append(arr[i][0])
        ans.append(arr[i][1])
    return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        intervals = list(map(int, input().split()))
        res = mergeIntervals(intervals, n)
        for i in res:
            print(i, end=' ')
        print()