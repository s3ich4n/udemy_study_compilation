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

    def run(
        self,
        k: int,
    ):
        return self.select(
            self.first_index,
            self.last_index,
            k - 1,
        )

    def partition(
        self,
        first_index,
        last_index,
    ):
        pivot_index = random.randint(first_index, last_index)

        self.swap(pivot_index, last_index)

        for i in range(first_index, last_index):
            if self.nums[i] < self.nums[last_index]:
                self.swap(i, first_index)
                first_index += 1

        self.swap(first_index, last_index)

        # 피벗 인덱스값을 리턴한다.
        return first_index

    def select(
        self,
        first_index,
        last_index,
        k,
    ):
        pivot_index = self.partition(first_index, last_index)

        # 좌측을 다 날림
        if pivot_index < k:
            return self.select(pivot_index + 1, last_index, k)

        # 우측을 다 날림
        elif pivot_index > k:
            return self.select(first_index, pivot_index - 1, k)

        # 값을 찾음
        else:
            return self.nums[k]


x = [1, 2, -5, 10, 100, -7, 3, 4]
select = QuickSelect(x)
print(select.run(4))
