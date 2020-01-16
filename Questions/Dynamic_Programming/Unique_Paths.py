# Link: https://leetcode.com/problems/unique-paths/submissions/
# Level: Medium

# Runtime: 32 ms, faster than 73.04% of Python3 online submissions for Unique Paths.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Unique Paths.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def memoize(func):
            memo = {}
            def helper(x,y):
                if (x,y) not in memo:
                    memo[(x,y)] = func(x,y)
                return memo[(x,y)]
            return helper

        @memoize

        def recurHelper(x,y):
            if x > m:
                return 0
            if y > n:
                return 0
            if x == m and y == n:
                return 1
            return recurHelper(x+1,y) + recurHelper(x,y+1)

        return recurHelper(1,1)
