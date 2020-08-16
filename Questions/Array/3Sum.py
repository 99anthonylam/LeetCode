# Link: https://leetcode.com/problems/3sum/
# Difficulty: Medium

# Runtime: 1756 ms, faster than 21.09% of Python3 online submissions for 3Sum.
# Memory Usage: 17 MB, less than 87.86% of Python3 online submissions for 3Sum.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1  
        return ans