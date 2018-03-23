'''
https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Given a binary tree, return the preorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # a list to contain the answer
        answer = []

        # if root is null, return empty list
        if not root:
            return answer

        # the first node is root
        current = root

        # Use a stack to contain all the nodes that have children to visit still
        stack = [root]

        # while there are still nodes in the stack
        while stack:

            # while the current node is not None
            while current:

                # append the value to the answer
                answer.append(current.val)

                # store the node in the stack in case it has children
                stack.append(current)

                # go to the left
                current = current.left
            
            # when a left node is None, we take the last node with possible children from the stack and go to its right
            current = stack.pop().right

        # When there's no more nodes to pop from the stack, return the answer
        return answer