# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium

# Runtime: 36 ms, faster than 93.89% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 13.9 MB, less than 87.95% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l<r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target <= nums[r-1] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        return -1

