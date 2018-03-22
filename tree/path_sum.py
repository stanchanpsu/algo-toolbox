'''
https://leetcode.com/problems/path-sum/description/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countPathSum(self, node, count):
        # if the node is None, then it is not a leaf node -> path invalid
        if node is None:
            return False

        # Add the node.val to the count
        count = count + node.val

        # If the node has no children it is a leaf node
        if node.left is None and node.right is None:

            # Return whether the path sum to this leaf node is the target sum
            return count == self.sum

        # recursively check all left and right children nodes, just return if either is True and let the True bubble up
        return self.countPathSum(node.left, count) or self.countPathSum(node.right, count)

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # store the sum for easy access
        self.sum = sum
        return self.countPathSum(root, 0)