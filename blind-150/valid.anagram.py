"""
[EASY] Valid Anagram
__________________________

Problem: Given two strings s and t, return true if the two strings
are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as
another string, but the order of the characters can be different.

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if sorted(s) == sorted(t):
            return True

        return False



Example_1 = Solution()
print(Example_1.isAnagram(s = "racecar", t = "carrace"))

Example_2 = Solution()
print(Example_2.isAnagram(s = "jar", t = "jam"))


"""
Examples:
__________________________
Example 1:

Input: s = "racecar", t = "carrace"
Output: true
----------

Example 2:

Input: s = "jar", t = "jam"
Output: false
----------
----------
Constraints:

s and t consist of lowercase English letters.
"""