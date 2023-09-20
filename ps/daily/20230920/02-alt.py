#
# https://leetcode.com/problems/maximum-subarray/
#
#
# 지금 이 방식을 divide and conquer로 ?
#


import pathlib
import sys

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0

        for idx in nums:
            current_sum = max(idx, current_sum + idx)
            best_sum = max(best_sum, current_sum)

        return best_sum


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([-1]))
with open(pathlib.Path().cwd() / "02-case1", "r") as f:
    print(s.maxSubArray(nums=eval(f.readline())))
