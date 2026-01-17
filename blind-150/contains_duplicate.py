"""
[EASY] Contains Duplicate
__________________________

Problem: Given an integer array nums,
return true if any value appears more than
once in the array, otherwise return false.

"""
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = 0
        for num in nums:
            count = nums.count(num)
            if count > 1:
                dups += 1
            else:
                pass

        if dups > 0:
            return True
        else:
            return False

Example_1 = Solution()
print(Example_1.hasDuplicate(nums = [1, 2, 3, 3]))

Example_2 = Solution()
print(Example_2.hasDuplicate(nums = [1, 2, 3, 4]))

"""
Expected Outcome:
__________________________
Example 1:

Input: nums = [1, 2, 3, 3]
Output: True
----------

Example 2:

Input: nums = [1, 2, 3, 4]
Output: False

"""