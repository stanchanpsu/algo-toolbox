'''
https://leetcode.com/problems/binary-tree-paths/description/

Given a binary tree, return all root-to-leaf paths.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPath(self, node, path):

        # If node is None, went beyond path
        if node is None:
            return

        # Add node.val to path
        path = path + '->' + str(node.val)

        # If leaf node, append the path to self.paths
        if not node.left and not node.right:
            self.paths.append(path)

        # Recursively check all children
        self.findPath(node.left, path)
        self.findPath(node.right, path)
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # Special cases for root is none is root is also a leaf
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        # Make attribute to store paths
        self.paths = []

        # Recursively check all children
        self.findPath(root.left, str(root.val))
        self.findPath(root.right, str(root.val))
        return self.paths