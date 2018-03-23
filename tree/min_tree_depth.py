'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # If root is null min path is 0
        if not root:
            return 0
        # Weirdly, if root has no children, min path is 1
        if not root.left and not root.right:
            return 1

        # breadth first search
        this = [root]
        counter = 0
        while this:
            counter = counter + 1
            next_row = []
            for node in this:
                if node.left: next_row.append(node.left)
                if node.right: next_row.append(node.right)

                # At any time if a node doesn't have children, return the counter. Because this is iterative solution, the first return will be the min depth
                if not node.left and not node.right:
                    return counter
            this = next_row
        
        # Should never return here
        return counter