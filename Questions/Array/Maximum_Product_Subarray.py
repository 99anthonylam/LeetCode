# Link: https://leetcode.com/problems/maximum-product-subarray/submissions/
# Level: Medium

# Runtime: 48 ms, faster than 93.82% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Maximum Product Subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sneg,lneg,numneg,zeroes = len(nums),0,0,[]
        for i,val in enumerate(nums):
            if val < 0:
                numneg += 1
                if i < sneg:
                    sneg = i
                if i > lneg:
                    lneg = i
            if val == 0:
                zeroes.append(i)
        if len(zeroes) > 0:
            potans = [0]
            s = 0
            for z in zeroes:
                potans.append(self.maxProduct(nums[s:z]))
                s = z+1
            if s != len(nums):
                potans.append(self.maxProduct(nums[s:]))
            if any(nums):
                return max(potans)
            return 0
        else:
            if numneg % 2 == 0:
                ans = 1
                for x in nums:
                    ans *= x
                return ans
            else:
                if len(nums) == 1:
                    return nums[0]
                ans = float("-inf")
                if lneg > 0:
                    ans = 1
                    for i in range(0,lneg):
                        ans *= nums[i]
                ans2 = float("-inf")
                if sneg < len(nums)-1:
                    ans2 = 1
                    for i in range(sneg+1,len(nums)):
                        ans2 *= nums[i]
                if ans > ans2:
                    return ans
                return ans2