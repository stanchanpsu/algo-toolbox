'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given a linked list, remove the nth node from the end of list and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # Use two pointers
        first = head
        second = head
        length = 0

        # Find the length of the entire list
        while first:
            length += 1
            first = first.next

        # Where the second pointer needs to get to
        m = length - n - 1

        # If length is not 0 or (n == l) which would mean removing the first node
        # We actually assume for this entire solution that length is at least 1
        if m >= 0:
            # Get second pointer to m position
            for i in range(0, m):
                second = second.next
            # Delete the m node
            second.next = second.next.next

            # Return the list
            return head

        # If we want to remove the first node then just return head.next
        else:
            return head.next