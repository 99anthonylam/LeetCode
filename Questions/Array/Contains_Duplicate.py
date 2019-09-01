# Link: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy

# Runtime: 132 ms, faster than 97.60% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 19.2 MB, less than 16.98% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        return len(nums) != len(set(nums))
