# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left_prod = right_prod = 1
        
        # multiply from left side
        for val in nums:
            output.append(left_prod)
            left_prod *= val
        
        # multiply from right side
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right_prod
            right_prod *= nums[i]
                       
        return output
