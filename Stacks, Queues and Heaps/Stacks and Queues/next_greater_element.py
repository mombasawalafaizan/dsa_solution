from collections import deque

def nextGreaterElement(arr, n):
    if n == 0:
        return []
    res = [-1] * n
    stack = deque()
    stack.append(0)
    for i in range(1, n):
        next = arr[i]
        if stack:
            element_idx = stack.pop()
            while arr[element_idx] < next:
                res[element_idx] = next
                if not stack:
                    break
                element_idx = stack.pop()
            
            if arr[element_idx] > next:
                stack.append(element_idx)
        stack.append(next)
    return arr

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        res = nextGreaterElement(arr, n)
        for i in res:
            print(i, end=' ')
        print()