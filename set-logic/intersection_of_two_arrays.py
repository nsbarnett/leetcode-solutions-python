"""
[EASY] 349. Intersection of Two Arrays
__________________________

Problem: Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        return list(nums1 & nums2) # Using set intersection operator '&'
    
test = Solution()

"---------------------------------------------------------"
" EXAMPLE 1:"
# Expected output: [2]       
print(test.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))

"---------------------------------------------------------"
" EXAMPLE 2:"
# Expected output: [9,4]    
print(test.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))      


"""
Set operations:
| = union of sets     
& = intersection of sets
- = difference between sets
^ = in first or second set, but not both

ex:
set1 = {1, 2, 3, 4}
set2 = {1, 5}

set1 | set2 = {1,2,3,4,5}
set1 & set2 = {1}
set1 - set2 = {2,3,4}
set1 ^ set2 = {2,3,4,5}

"""
