# Link: https://leetcode.com/problems/valid-palindrome/
# Level: Easy

# Runtime: 48 ms, faster than 80.16% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 13.2 MB, less than 94.05% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and r > l:
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
