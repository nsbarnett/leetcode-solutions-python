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

solution_1 = Solution()
solution_2 = Solution()
solution_3 = Solution()

solution_1.twoSum(nums = [3,4,5,6], target = 7)
solution_2.twoSum(nums = [4,5,6], target = 10)
solution_3.twoSum(nums = [5,5], target = 10)