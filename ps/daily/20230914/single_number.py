#
# https://leetcode.com/problems/single-number/
#


import collections

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)

        return c.most_common()[-1][0]


s = Solution()
s.singleNumber([2,2,1])
s.singleNumber([4,1,2,1,2])
s.singleNumber([1])
