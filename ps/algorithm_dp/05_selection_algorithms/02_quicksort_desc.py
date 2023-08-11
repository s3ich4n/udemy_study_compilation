# https://en.wikipedia.org/wiki/Quicksort
# Hoare partition scheme을 구현함
import random

from typing import List


class QuickSelect:

    def __init__(
        self,
        nums: List[int],
    ) -> None:
        self.nums = nums
        self.first_index = 0
        self.last_index = len(nums) - 1

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def quicksort(
        self,
        first_index,
        last_index,
    ):
        if first_index >= 0 and last_index >= 0 and first_index < last_index:
            p = self.partition(first_index, last_index)
            self.quicksort(first_index, p)
            self.quicksort(p + 1, last_index)

    def partition(
        self,
        first_index,
        last_index,
    ):
        pivot = self.nums[(first_index + last_index) // 2]
        i = first_index - 1
        j = last_index + 1

        # do while을 구현할 방법이 없어서 논리를 풀어서 씀
        # 아래 while 구문의 등호에 따라 정순/역순 정렬을 함
        while True:
            i += 1
            while self.nums[i] < pivot:
                i += 1
            j -= 1
            while self.nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            self.swap(i, j)


x = [1, 2, -5, 10, 100, -7, 3, 4]
select = QuickSelect(x)
select.quicksort(select.first_index, select.last_index)
print(select.nums)
