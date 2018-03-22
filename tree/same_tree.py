'''
https://leetcode.com/problems/same-tree/description/

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameNode(self, p, q):
        
        # If node p and q are both None, then they are identical
        if (p is None and q is None):
            return True

        # If only p or q is None or the values differ, they are not the same
        if p is None or q is None or p.val != q.val:
            return False

        # Recursively check all children nodes
        left = self.isSameNode(p.left, q.left)
        right = self.isSameNode(p.right, q.right)

        # Both left and right have to always return True for the tree to be identical
        if (not left or not right):
            return False
        else:
            return True
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.isSameNode(p, q)