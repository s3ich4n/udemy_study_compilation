#
# https://leetcode.com/problems/two-sum/
#


import collections

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #
        # 순서가 있다
        # 동일한 변수를 두 번 사용해서 더하는게 아니다
        # 정렬되어있지 않다
        #
        cur_pos = 1

        for val in nums:
            for find_pos in range(cur_pos, len(nums)):
                if val + nums[find_pos] == target:
                    return [(cur_pos) - 1, (find_pos + 1) - 1]
            cur_pos += 1


s = Solution()
print(s.twoSum(nums=[3,2,4], target=6))
print(s.twoSum(nums=[2,7,11,15], target=9))
print(s.twoSum(nums=[3,3], target=6))
