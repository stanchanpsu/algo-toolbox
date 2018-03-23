'''
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        answer = []
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # If root is none, return empty list
        if not root:
            return answer

        # make first level containing only root node
        this_row = [root]

        # while this level has ndoes
        while this_row:

            # make list to store level values
            this_row_values = []

            # make list to store next level
            next_row = []

            # for evey node in this level
            for node in this_row:
                # store its value
                this_row_values.append(node.val)

                # if there are children put it in the next level
                if node.left: next_row.append(node.left)
                if node.right: next_row.append(node.right)

            # append this levels values to the final answer list
            answer.append(this_row_values)

            # the new this_row is the next_row
            this_row = next_row

        # Once a level has no more nodes the answer is done
        return answer