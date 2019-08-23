# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Level: Medium

# Runtime: 48 ms, faster than 91.51% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.5 MB, less than 6.90% of Python3 online submissions for Validate Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(node, lo, hi):
            if not node:
                return True
            elif lo < node.val < hi:
                tmp_left = helper(node.left, lo, node.val) if node.left else True
                tmp_right = helper(node.right, node.val, hi) if node.right else True
                return tmp_left and tmp_right
            else:
                return False
        
        return helper(root, -sys.maxsize, sys.maxsize)
        