# Link: https://leetcode.com/problems/climbing-stairs/submissions/
# Difficulty: Easy

# Runtime: 36 ms, faster than 65.90% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.7 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.

class Solution:

    def climbStairs(self, n: int) -> int:
        arr = [None] * (n+1)

        def helper(n):
            if n <= 1:
                return 1
            if not arr[n]:
                arr[n] = helper(n-1) + helper(n-2)
            return arr[n]

        return helper(n)
