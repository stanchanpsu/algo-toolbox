# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # If the node is none do nothing
        if not root:
            return
        # swap the children
        root.left, root.right = root.right, root.left

        # recursively
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root