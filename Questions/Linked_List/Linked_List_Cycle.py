# Link: https://leetcode.com/problems/linked-list-cycle/
# Level: Easy

# Runtime: 48 ms, faster than 63.30% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # seen = {}
        # while head is not None:
        #     if head in seen:
        #         return True
        #     else:
        #         seen[head] = True
        #     head = head.next
        # return False

        while head is not None:
            if head == "STOP":
                return True
            else:
                temp = head
                head = head.next
                temp.next = "STOP"
        return False
