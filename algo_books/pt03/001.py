from typing import List


class Quiz001:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]


if __name__ == "__main__":
    q = Quiz001()

    nums = [7, 12, 11, 15, 6, 2, 67, 23, 99, 15]
    target = 21

    print(q.two_sum(nums, target))
