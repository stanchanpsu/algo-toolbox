'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, count):

        # Return the count if the node is None
        if node is None:
            return count

        # Else increment the count by 1 and return the check the children nodes for the maximum depth
        else:
            count = count + 1
            return max(self.traverse(node.left, count), self.traverse(node.right, count))
            
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root, 0)