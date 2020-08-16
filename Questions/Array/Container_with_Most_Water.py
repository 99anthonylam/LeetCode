# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium

# Runtime: 124 ms, faster than 93.01% of Python3 online submissions for Container With Most Water.
# Memory Usage: 15.2 MB, less than 96.93% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ans = 0, len(height) - 1, -1
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans