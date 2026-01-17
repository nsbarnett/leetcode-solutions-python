"""
[EASY] Two Sum
__________________________

Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, X in enumerate(nums):
            for j, Y in enumerate(nums):
                if (i != j) and (X + Y) == target:
                    return [i, j]

test = Solution() # set instance for class Solution

# output test cases for the twoSum method
print(test.twoSum( nums=[2,7,11,15], target=9))
print(test.twoSum( nums=[3,2,4], target=6))
print(test.twoSum( nums=[3,3], target=6))