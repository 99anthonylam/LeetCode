# Link: https://leetcode.com/problems/group-anagrams/
# Level: Medium

# Runtime: 104 ms, faster than 79.24% of Python3 online submissions for Group Anagrams.
# Memory Usage: 16.8 MB, less than 41.51% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            chars = tuple(sorted(str))
            if chars in dict:
                dict[chars].append(str)
            else:
                dict[chars] = [str]
        return dict.values()
