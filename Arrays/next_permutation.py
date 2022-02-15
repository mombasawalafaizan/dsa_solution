from typing import List
import random

def findLeastGreaterElementPosition(arr, x, l, h):
    mid = 0
    while l<h:
        mid = (l+h)//2
        if arr[mid] > x:
            if arr[mid+1] <= x:
                return mid
            l = mid+1
        else:
            h = mid
    return l

def nextPermutation( nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i = n-1
        while i>=0:
            if i==0:
                return nums[-1::-1]
            if nums[i-1]>=nums[i]:
                i -= 1
            else:
                print(i)
                j = findLeastGreaterElementPosition(nums, nums[i-1], i, n-1)
                print(j)
                print()
                nums[i-1], nums[j] = nums[j], nums[i-1]
                return nums[:i] + nums[n-1:i-1:-1]
        return []

# initial = [1, 1, 5]
# for i in range(6):
#     print(initial)
print(nextPermutation([1, 5, 1]))
# a = [random.randint(1, 100) for i in range(10)]
# a.sort(reverse=True)
# print([*enumerate(a)])
# #a=[ 0,  1,  2,  3,  4,  5,  6,  7,  8, 9]
# for i in range(10):
#     temp = random.randint(-10, 105)
#     print('find: ', temp)
#     print(findLeastGreaterElementPosition(a, temp, 0, 9))
