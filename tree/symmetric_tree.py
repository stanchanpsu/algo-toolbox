'''
https://leetcode.com/problems/symmetric-tree/description/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def matches(self, left, right):
        # If both left and right nodes are None, they are symmetric
        if left is None and right is None:
            return True

        # If only left or right nodes are None or their values differ, they are not symmetric
        if left is None or right is None or left.val != right.val:
            return False
        
        # Recursively check the entire tree comparing the left's left children to the right's right children and the left's right children to the right's left children
        return self.matches(left.left, right.right) and self.matches(left.right, right.left)
        
    def isSymmetric(self, root):

        """
        :type root: TreeNode
        :rtype: bool
        """
        # If the root node is None, it is symmetric
        if root is None:
            return True
        return self.matches(root.left, root.right)