"""
[EASY] Linked List Cycle
__________________________

Problem: Given the head of a singly linked list, reverse the list, and return the reversed list.

"""

# Definition for singly-linked list.
class LinkedNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

""" This solution iterates through the linked list at a fast and slow pace.
    If there is a cycle, the fast iteration will catch the sow iteration.
    If not, a next=None consition will break the loop.  """

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

"---------------------------------------------------------"
" EXAMPLE 1:"       
# Create nodes
a = LinkedNode(3)
b = LinkedNode(2)
c = LinkedNode(0)
d = LinkedNode(-4)

# Link nodes
a.next = b
b.next = c
c.next = d
d.next = b  # Creates a cycle here back to node b

# Create solution instance
test = Solution()

# Test hasCycle function
print("Example 1 has cycle: " + str(test.hasCycle(a)))  # Expected output: True

"---------------------------------------------------------"
" EXAMPLE 2:"       
# Create nodes
a = LinkedNode(1)
b = LinkedNode(2)

# Link nodes
a.next = b
b.next = a  # Creates a cycle here back to node b

# Create solution instance
test = Solution()

# Test hasCycle function
print("Example 2 has cycle: " + str(test.hasCycle(a)))  # Expected output: True

"---------------------------------------------------------"
" EXAMPLE 3:"       
# Create nodes
a = LinkedNode(1)

# Create solution instance
test = Solution()

# Test hasCycle function
print("Example 3 has cycle: " + str(test.hasCycle(a)))  # Expected output: False

"---------------------------------------------------------"