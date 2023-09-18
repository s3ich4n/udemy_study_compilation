#
# https://leetcode.com/problems/longest-happy-prefix/
#


class Solution:
    def longestPrefix(self, s: str) -> str:
        def prefix(left, right, limit):
            result = ""

            if s[:left] == s[right:]:
                result = s[:left]

            return result

        if len(s) == 1:
            return ""

        answer = ""
        left, right, limit = 0, len(s), 1

        while limit < len(s) + 1:
            answer = max(answer, prefix(left, right, limit))
            left += 1
            right -= 1
            limit += 1

        return answer


s = Solution()
print(s.longestPrefix("level"))
print(s.longestPrefix("ababab"))
print(s.longestPrefix("aaaaa"))
