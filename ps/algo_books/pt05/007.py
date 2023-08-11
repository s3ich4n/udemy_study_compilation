import sys
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _do_search(data: List[int]):
            current = len(data) // 2
            try:
                if len(data) == 1:
                    if data[current] != target:
                        return -sys.maxsize

                if data[current] == target:
                    return data[current]

                elif data[current] > target:
                    return _do_search(data[:current])

                elif data[current] < target:
                    return _do_search(data[current:])

                else:
                    return -1

            except IndexError:
                return -1

        answer = _do_search(nums)

        if answer == -sys.maxsize:
            return -1
        else:
            return nums.index(answer)


s = Solution()
# print(s.search(nums=[-1,0,3,5,9,12], target=9))
# print(s.search(nums=[-1,0,3,5,9,12], target=2))
print(s.search(nums=[-1,0,5], target=-1))
