#
# https://leetcode.com/problems/find-the-difference/
#


import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        answer = collections.defaultdict(int)

        for char in s:
            answer[char] += 1

        for char in t:
            answer[char] -= 1

        return sorted(answer.items(), key=lambda x: x[1])[0][0]


s = Solution()
print(s.findTheDifference(s="abcd", t="abcde"))
print(s.findTheDifference(s="", t="y"))
print(s.findTheDifference(s="ae", t="aea"))
