#
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
#


import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        s_count = collections.defaultdict(int)
        s_endpoint = {}
        d = {}

        # 3.7부터는 순서를 보장하니까...
        for idx, i in enumerate(s):
            s_count[i] += 1
            s_endpoint[i] = idx

        a = collections.Counter(s_count)


        # case 2에 대한 로직
        prev_v = None
        for k, v in a.most_common():
            print(k, v)
            if v == prev_v:
                del s_count[k]
            prev_v = v

        # case 1에 대한 로직
        b = 1

        return -1


s = Solution()
# print(s.minDeletions("aab"))
print(s.minDeletions("aaabbbcc"))
# print(s.minDeletions("ceabaacb"))
