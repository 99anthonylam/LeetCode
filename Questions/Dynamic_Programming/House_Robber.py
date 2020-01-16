# Link: https://leetcode.com/problems/house-robber/
# Level: Easy

# Runtime: 28 ms, faster than 90.90% of Python3 online submissions for House Robber.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for House Robber.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_money = [0 for _ in nums]
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        else:
            max_money[0] = nums[0]
            max_money[1] = nums[1]
            for i, house in enumerate(nums[2:]):
                    max_money[i+2] = max(house, house + max(max_money[:i+1]))
            return max(max_money[len(nums)-1], max_money[len(nums)-2])
