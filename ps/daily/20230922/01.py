#
# https://leetcode.com/problems/is-subsequence/
#
# 어프로치 #1
#   가면서 있는지 계속 물어본다.
#   이미 한 번 지나가버리면 "aec" 와 같은 케이스인 것으로 가정하고 포기한다.
#


import pathlib


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True

        subsequence = 0
        for ch in t:
            if subsequence <= len(s) - 1:   # 이 이상 길어질 일이 없기때문
                if s[subsequence] == ch:
                    subsequence += 1
        
        return subsequence == len(s)


s = Solution()
print(s.isSubsequence(s="abc", t="ahbgdc"))   # 예상결과: true
print(s.isSubsequence(s="axc", t="ahbgdc"))   # 예상결과: false
print(s.isSubsequence(s="ab", t="baab"))      # 예상결과: true
print(s.isSubsequence(s="abc", t="acb"))      # 예상결과: false
with open(pathlib.Path().cwd() / "testcase17", "r") as f:
    print(s.isSubsequence(
        s="leeeeetcode",
        t=f.readline(),
    ))  # 예상결과: true
