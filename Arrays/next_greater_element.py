from collections import deque

def getNGE(arr):
    """Function returns an array containing the next greater element for each element
    passed in the list of argument array"""
    nge = [-1] * len(arr)
    stack = deque()
    stack.append(0)
    idx = 0
    next_g = 0
    for i in range(1, len(arr)):
        next_g = arr[i]
        if stack:
            idx = stack.pop()
            while arr[idx] < next_g:
                nge[idx] = next_g
                if not stack:
                    break
                idx = stack.pop()

            if arr[idx] > next_g:
                stack.append(idx)
        stack.append(i)
    return nge

if __name__ == "__main__":
    a = [90, 62, 37, 46, 70, 26, 27, 91, 14, 58]
    print(a)
    print(getNGE(a))