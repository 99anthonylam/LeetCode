# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Easy

# Runtime: 72 ms, faster than 92.72% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.7 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)