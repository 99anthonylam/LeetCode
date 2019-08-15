# Runtime: 52 ms, faster than 96.32% of Python3 online submissions for Two Sum.
# Memory Usage: 15 MB, less than 9.06% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in dict:
                return [dict[diff],i]
            dict[val]=i
