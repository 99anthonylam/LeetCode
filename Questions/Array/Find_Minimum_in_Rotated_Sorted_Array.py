# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium 

# Runtime: 40 ms, faster than 79.42% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.1 MB, less than 44.12% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while nums[left] > nums[right]:
            left += 1
        return nums[left]