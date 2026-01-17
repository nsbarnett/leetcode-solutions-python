"""
[EASY] Majority Element
__________________________

Problem: Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

"""

from typing import List
import statistics


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return statistics.mode(nums)
        
""" There are various ways to solve this provblem, but for me, 'mode' provides
    the most readable syntax. """


test = Solution() # set instance for class Solution

# output test cases for the twoSum method
print(test.majorityElement( nums = [3,2,3]))
print(test.majorityElement( nums = [2,2,1,1,1,2,2]))