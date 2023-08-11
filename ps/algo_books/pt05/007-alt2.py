import bisect

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index >= len(nums) or nums[index] != target:
            return -1

        return index


s = Solution()
# print(s.search(nums=[-1,0,3,5,9,12], target=9))
# print(s.search(nums=[-1,0,3,5,9,12], target=2))
# print(s.search(nums=[-1,0,5], target=-1))
s.search(nums=[-1,0,3,5,9,12], target=13)
