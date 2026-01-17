"""
[MEDIUM] 3Sum
__________________________

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output
and the triplets in any order.

"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        trips = []

        for i, val_i in enumerate(nums):
            for j, val_j in enumerate(nums):
                for k, val_k in enumerate(nums):
                    if ((val_i + val_j + val_k) == 0) and (sorted([val_i,val_j,val_k]) not in trips):
                        if i == j or j == k or k == i: pass
                        else: trips.append(sorted([val_i,val_j,val_k]))
        return trips
    

"""
Examples:
__________________________
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
----------

Example 2:

Input: nums = [0,1,1]
Output: []
----------

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]

"""