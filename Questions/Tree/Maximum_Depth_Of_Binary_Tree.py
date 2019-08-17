# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy

# Runtime: 52 ms, faster than 44.48% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16 MB, less than 12.50% of Python3 online submissions for Maximum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
