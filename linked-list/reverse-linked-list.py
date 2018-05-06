'''
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Take care of the edge case
        if not head:
            return head

        # Use 2 pointers
        p1 = head
        p2 = head.next

        # set the end of the new list to None
        head.next = None
        

        # While p2 is not the original end
        while p1 and p2:

            # In place swap the nodes and pointers
            p2.next, p2, p1 = p1, p2.next, p2

        # Return the new head
        return p1