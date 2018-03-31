'''
https://leetcode.com/problems/swap-nodes-in-pairs/description/


Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        H = ListNode(0) #pylint: disable=E0602
        H.next = head
        first = H
        second = head
        while second and second.next:
            third = second.next
            second.next = third.next
            third.next = second
            first.next = third
            first = second
            second = second.next
        return H.next