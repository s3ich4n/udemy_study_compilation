from typing import List


class Solution:
    @staticmethod
    def _sort(x1: int, x2: int):
        return str(x1) + str(x2) > str(x2) + str(x1)

    def largestNumber(self, nums: List[int]) -> str:
        """
        어프로치 (교재)
        - 각 요소 단위로 크기 순으로 정렬
            - 9, 8, ... 1 순으로
            - 99, 98, ... 1 순으로 정렬
            - 9보다 99가 앞에
        - 배열을 그런 식으로 정렬하고, 전부 꺼내서 문자열화

        나머지는 Wikipedia에 있는 삽입 정렬을 따라서 구현했음.
        """

        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self._sort(nums[j], nums[j - 1]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int("".join(map(str, nums))))


s = Solution()
print(s.largestNumber(nums=[10,2]))
print(s.largestNumber(nums=[3,30,34,5,9]))
print(s.largestNumber(nums=[0,0]))
