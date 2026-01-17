"""
[MEDIUM] Group Anagrams
__________________________

Problem: Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # specify default factory (list)

        for word in strs:
            key = tuple(sorted(word)) # make hashable
            groups[key].append(word)

        return list(groups.values()) # clean up output. Otherwise would say 'defaultdict(<class 'list'>, {(): ['']})'


test = Solution() # set instance for class Solution

# output test cases for the twoSum method
print(test.groupAnagrams( strs = ["eat","tea","tan","ate","nat","bat"] ))
print(test.groupAnagrams( strs = [""] ))
print(test.groupAnagrams( strs = ["a"] ))