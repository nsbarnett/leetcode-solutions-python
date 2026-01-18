"""
[EASY] Merge Two Sorted Linked Lists
__________________________

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head
of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        values = []

        while list1:
            values.append(list1.val)
            list1 = list1.next

        while list2:
            values.append(list2.val)
            list2 = list2.next

        if not values:
            return None

        values_sorted = sorted(values)

        head = ListNode(values_sorted[0])
        current = head

        for value in values_sorted[1:]:
            current.next = ListNode(value)
            current = current.next

        return head
    
    
""" Leetcode treats the test inputs as linked list instead of the provided arrays. In order to have a solution run
    and provide the proper output, the test inputs would need to be constructed as linked list first run through the soltion.

    For simplicity, this solution does not provide the extra step of creating the linked list to run outside of leetcode.
"""   

"""
Examples:
__________________________
Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]
----------

Example 2:

Input: list1 = [], list2 = [1,2]
Output: [1,2]
----------

Example 3:

Input: list1 = [], list2 = []
Output: []

"""