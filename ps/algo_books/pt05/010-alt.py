import pathlib
import pickle
import bisect

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        어프로치 (2) - 이진탐색
        - 현재 값을 기준으로 나머지 값이 맞는지 찾기
        - 현재값을 기준으로 잡고, 이진탐색을 수행하기
        """
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return [k + 1, mid + 1]


s = Solution()
# print(s.twoSum(numbers=[2,7,11,15], target=9))
# print(s.twoSum(numbers=[2,3,4], target=6))
# print(s.twoSum(numbers=[2,25,75], target=100))
# print(s.twoSum(numbers=[3,24,50,79,88,150,345], target=200))
print(s.twoSum(numbers=[1,2,3,4,4,9,56,90], target=8)) # [4, 5]가 정답

with open(pathlib.Path().cwd() / "010-case", "r") as f:
    print(
        s.twoSum(
            numbers=eval(f.readline()),
            target=5,
        )
    )  # [13011, 13012]
