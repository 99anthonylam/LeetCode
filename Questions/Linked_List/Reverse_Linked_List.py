# Link: https://leetcode.com/problems/reverse-linked-list/solution/
# Difficulty: Easy

# Runtime: 36 ms, faster than 95.71% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15 MB, less than 31.82% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            temp, head.next = head.next, last
            last, head = head, temp
        return last
