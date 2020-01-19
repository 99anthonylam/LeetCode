# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium    

# Runtime: 48 ms, faster than 78.20% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 16.8 MB, less than 98.18% of Python3 online submissions for Kth Smallest Element in a BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        smalls = []
        
        def inorder(root):
            if len(smalls) == k:
                return 
            if root: 
                inorder(root.left) 
                smalls.append(root.val)
                inorder(root.right) 
                
        inorder(root)
        return smalls[k-1]
