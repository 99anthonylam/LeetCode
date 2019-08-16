# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium

# Runtime: 136 ms, faster than 80.14% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.4 MB, less than 82.00% of Python3 online submissions for Product of Array Except Self.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left_prod = right_prod = 1

        # multiply from left side
        for i in range(len(nums)):  # faster than for each loop
            output.append(left_prod)
            left_prod *= nums[i]

        # multiply from right side
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right_prod
            right_prod *= nums[i]

        return output
