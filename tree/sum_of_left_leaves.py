'''
https://leetcode.com/problems/sum-of-left-leaves/description/

Find the sum of all left leaves in a given binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isLeft(self, node, answer):
        if not node:
            return answer
        if not node.left and not node.right:
            answer = answer + node.val
        answer = self.isLeft(node.left, answer)
        return self.isRight(node.right, answer)
    def isRight(self, node, answer):
        if not node:
            return answer
        answer = self.isLeft(node.left, answer)
        return self.isRight(node.right, answer)
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.isLeft(root.left, 0)
        right = self.isRight(root.right, 0)
        return left + right