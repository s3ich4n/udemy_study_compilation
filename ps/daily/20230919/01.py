#
# https://leetcode.com/problems/find-the-duplicate-number/
#


import collections

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = collections.defaultdict(int)

        for idx in nums:
            dup[idx] += 1

            if dup[idx] != 1:
                return idx


s = Solution()
print(s.findDuplicate(nums=[1,3,4,2,2]))
print(s.findDuplicate(nums=[3,1,3,4,2]))
