#
# https://leetcode.com/problems/valid-anagram/
#


import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_data = collections.defaultdict(int)
        c_data = collections.defaultdict(int)

        for c in s:
            s_data[c] += 1

        for c in t:
            c_data[c] += 1
        
        if s_data != c_data:
            return False

        return True


s = Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))
print(s.isAnagram(s = "rat", t = "car"))
print(s.isAnagram(s = "a", t = "ab"))
