from collections import deque

def nextSmallerElement(arr):
    n = len(arr)
    res = [-1] * n
    stack = deque()
    stack.append(0)
    for i in range(1, n):
        next = arr[i]
        if stack:
            idx = stack.pop()
            while next < arr[idx]:
                res[idx] = next
                if not stack:
                    break
                idx = stack.pop()
            if arr[idx] < next:
                stack.append(idx)
        stack.append(i)
    return arr

nextSmallerElement([4, 8, 5, 2, 25])