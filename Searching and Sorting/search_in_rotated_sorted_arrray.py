from typing import List
class Solution:
    def getPivotIndex(self, nums: list):
        left, right = 0, len(nums) - 1
        while nums[left] > nums[right]:
            middle  = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        return left
    
    def binarySearch(self, arr, l, r, x): 
        while l <= r: 
            mid = (l + r)// 2; 
            if arr[mid] == x: 
                return mid
            elif arr[mid] < x: 
                l = mid + 1
            else: 
                r = mid - 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        """Find the element in left sorted array and right sorted array which is divided from           the pivot point, if target is in either array return the max of index of this element           and -1 and if not present return -1"""              
        if not nums:
            return -1
        pivot_idx = self.getPivotIndex(nums)
        print("PIVOT", pivot_idx)
        return max(self.binarySearch(nums, 0, pivot_idx - 1, target), self.binarySearch(nums, pivot_idx, len(nums) - 1, target))