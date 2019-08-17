# Link: https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy

# Runtime: 36 ms, faster than 73.03% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root
