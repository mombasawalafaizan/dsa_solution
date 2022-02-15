import random
from pprint import List

# Given a sorted integer array arr, two integers k and x, return the k closest integers
# to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b


def BS_right(arr, target):
    """This function returns the idx of rightmost target if found,
       else it returns the place where the element would be kept
       Similar to bisect_right"""
    n = len(arr)
    low = 0
    high = n-1
    while low < high:
        m = (low + high) // 2
        if arr[m] <= target:
            if arr[m] == target and m != n-1 and arr[m+1] != arr[m]:
                return m
            low = m + 1
        else:
            high = m
    return high


# Algorithm: Find the element nearest to x using Binary Search, then start from left
# and right insert the elements in the result based on the compare conditions
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    n = len(arr)
    if k == n:
        return arr[:]
    idx = BS_right(arr, x)
    i = idx - 1
    j = idx
    selected = 0
    res = []
    while selected < k and i >= 0 and j < n:
        if abs(arr[i]-x) <= abs(arr[j]-x):
            res.append(arr[i])
            i -= 1
        else:
            res.append(arr[j])
            j += 1
        selected += 1
    while selected < k and i >= 0:
        res.append(arr[i])
        selected += 1
        i -= 1
    while selected < k and j < n:
        res.append(arr[j])
        selected += 1
        j += 1
    return sorted(res)


arr = [random.randint(1, 30) for _ in range(20)]
arr.sort()
x = random.randint(1, 100)
for i in range(len(arr)):
    print("%-2d" % (arr[i]), end=' ')
print(x)
for i in range(len(arr)):
    print("%-2d" % (i), end=' ')
print()

print('ans', BS_right(arr, x))
