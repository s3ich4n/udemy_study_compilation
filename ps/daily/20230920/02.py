#
# https://leetcode.com/problems/maximum-subarray/
#


import pathlib
import sys

from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         answer = [0 for _ in range(len(nums))]
#         starting_point = 0
#         for kth, idx in enumerate(nums):
#             if idx < 0:
#                 if sum(nums[starting_point:kth]) + idx <= 0:
#                     answer[kth] = idx
#                     starting_point = kth + 1
#                 else:
#                     answer[kth] = sum(nums[starting_point:kth])
#             else:
#                 answer[kth] = idx + sum(nums[starting_point:kth])

#         return max(answer)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for idx in range(1, len(nums)):
            if nums[idx] + nums[idx - 1] < 0:
                nums[idx] = nums[idx]
            else:
                if nums[idx - 1] < 0:
                    nums[idx] = nums[idx]
                else:
                    nums[idx] = nums[idx] + nums[idx - 1]

        return max(nums)


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([-1]))
with open(pathlib.Path().cwd() / "02-case1", "r") as f:
    print(s.maxSubArray(nums=eval(f.readline())))
