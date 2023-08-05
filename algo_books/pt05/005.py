from typing import List


class Solution:
    def three_way_partition(self, A: List[int], mid: int):
        i = j = 0
        k = len(A)

        while j < k:
            if A[j] < mid:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1
            elif A[j] > mid:
                k -= 1
                A[j], A[k] = A[k], A[j]
            else:
                j += 1

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        어프로치 (교재)

        네덜란드 국기 문제임.
        퀵소트의 개선 아이디어와 비슷하다. <- 해당부분에 중점을 두자

        1. 3-way partitioning을 수행한다. (기존 퀵소트는 분할을 2개만 했었음)
        """

        self.three_way_partition(nums, 1)


s = Solution()
# s.sortColors(nums=[2, 1, 2, 0, 0, 1])
s.sortColors(nums=[2, 0, 1, 2, 1, 0])
s.sortColors(nums=[2, 0, 1])
