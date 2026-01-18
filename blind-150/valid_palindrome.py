"""
[EASY] Valid Palindrome
__________________________

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []

        for char in s.lower():
            if char.isalnum():
                letters.append(char)

        if letters == letters[::-1]:
            return True
        
        return False



Example_1 = Solution()
print(Example_1.isPalindrome(s = "Was it a car or a cat I saw?"))

Example_2 = Solution()
print(Example_2.isPalindrome(s = "tab a cat"))


"""
Examples:
__________________________
Example 1:

Input: s = "Was it a car or a cat I saw?"
Output: true
----------

Example 2:

Input: s = "tab a cat"
Output: false

"""