import pathlib
import pickle

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        어프로치 (1) - 투 포인터
        - 양 사이드로부터 시작해서...
        - 조건을 찾기 위해 두개의 포인터를 컨트롤하는게 투 포인터!
        """
        left, right = 0, len(numbers) - 1

        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]


s = Solution()
# print(s.twoSum(numbers=[2,7,11,15], target=9))
# print(s.twoSum(numbers=[2,3,4], target=6))
# print(s.twoSum(numbers=[2,25,75], target=100))
# print(s.twoSum(numbers=[3,24,50,79,88,150,345], target=200))
# print(s.twoSum(numbers=[1,2,3,4,4,9,56,90], target=8)) # [4, 5]가 정답

with open(pathlib.Path().cwd() / "010-case", "r") as f:
    print(
        s.twoSum(
            numbers=eval(f.readline()),
            target=5,
        )
    )  # [13011, 13012]
