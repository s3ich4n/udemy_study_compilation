from typing import List


class Solution:
    @staticmethod
    def _sort(x1: int, x2: int):
        return int(str(x1) + str(x2)) < int(str(x2) + str(x1))

    def insertion_sort(self, nums: List[int], cur: int):
        comparator = None

        if self._sort(nums[cur - 1], nums[cur]):
            comparator = cur
        else:
            comparator = cur - 1

        for idx in range(cur - 1, -1, -1):
            if self._sort(nums[idx], nums[comparator]):
                nums[idx], nums[comparator] = nums[comparator], nums[idx]
                comparator -= 1
            else:
                continue

    def largestNumber(self, nums: List[int]) -> str:
        """
        어프로치 (교재)
        - 각 요소 단위로 크기 순으로 정렬
            - 9, 8, ... 1 순으로
            - 99, 98, ... 1 순으로 정렬
            - 9보다 99가 앞에
        - 배열을 그런 식으로 정렬하고, 전부 꺼내서 문자열화
        """

        idx = 1
        while idx < len(nums):
            self.insertion_sort(nums, idx)
            idx += 1

        return str(int("".join(map(str, nums))))


s = Solution()
print(s.largestNumber(nums=[10,2]))
print(s.largestNumber(nums=[3,30,34,5,9]))
print(s.largestNumber(nums=[0,0]))
