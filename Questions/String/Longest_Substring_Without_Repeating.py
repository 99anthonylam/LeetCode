# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium

# Runtime: 48 ms, faster than 99.22% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        dic = {}  # dict with positions of each char
        a = b = 0  # start and end indices of current substring
        
        for i, val in enumerate(s):
            # if val is already in current substring (between a and b)
            if val in dic and dic[val] >= a:
                a = dic[val] + 1  # update substring to start after earlier occurence of val
                dic[val] = i 
                b += 1  # add val to substring
            else:
                dic[val] = i
                b += 1
                if b - a > longest:
                    longest = b - a

        return longest