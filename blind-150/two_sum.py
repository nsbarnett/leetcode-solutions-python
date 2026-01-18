"""
[EASY] Two Sum
__________________________

Given an array of integers nums and an integer target, return the
indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices
i and j that satisfy the condition.

Return the answer with the smaller index first.

"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val_i in enumerate(nums):
            for j, val_j in enumerate(nums):
                if i !=j and (val_i+val_j) == target:
                    return [i,j]



Example_1 = Solution()
print(Example_1.twoSum(nums = [3,4,5,6], target = 7))

Example_2 = Solution()
print(Example_2.twoSum(nums = [4,5,6], target = 10))

Example_3 = Solution()
print(Example_3.twoSum(nums = [5,5], target = 10))
    

"""
Examples:
__________________________
Example 1:

Input: nums = [3,4,5,6], target = 7
Output: [0, 1]
----------

Example 2:

Input: nums = [4,5,6], target = 10
Output: [0, 2]
----------

Example 3:

Input: nums = [5,5], target = 10
Output: [0, 1]

"""