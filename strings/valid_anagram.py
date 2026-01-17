"""
[EASY] Valid Anagram
__________________________

Problem: Given two strings s and t, return true if t is
an anagram of s, and false otherwise.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

test = Solution() # set instance for class Solution

# output test cases for the isAnagram method
print(test.isAnagram(s = "anagram", t = "nagaram"))
print(test.isAnagram(s = "rat", t = "car"))