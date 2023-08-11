import sys
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _do_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return _do_search(mid + 1, right)
                elif nums[mid] > target:
                    return _do_search(left, mid - 1)
                else:
                    return mid

            else:
                return -1

        return _do_search(0, len(nums) - 1)


s = Solution()
# print(s.search(nums=[-1,0,3,5,9,12], target=9))
# print(s.search(nums=[-1,0,3,5,9,12], target=2))
print(s.search(nums=[-1,0,5], target=-1))
