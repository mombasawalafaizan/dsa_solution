# Refer this page
# https://leetcode.com/problems/subsets/solution/

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    # Initialize a set with a NULL set already inserted in it
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]

    return output
