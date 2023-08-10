import bisect
import pathlib
import timeit

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        어프로치 (3) - bisect 를 통한 이진탐색 (1): 이해하고 구현하기
        1. numbers를 순회하면서 (k, v로) expected를 구하기
        2. numbers[k + 1:] 에서 expect와 가장 근접한 index를 구하기
        3. numbers 내의 인덱스 + (k + 1)값이 실제 expected인지 확인하기
        """
        for k, v in enumerate(numbers):
            expected = target - v
            splitted = numbers[k + 1:]
            i = bisect.bisect_left(splitted, expected)
            index_in_numbers = i + k + 1
            if i < len(splitted) and numbers[index_in_numbers] == expected:
                return [k + 1, (index_in_numbers) + 1]


s = Solution()
# print(s.twoSum(numbers=[2,7,11,15], target=9))
# print(s.twoSum(numbers=[2,3,4], target=6))
# print(s.twoSum(numbers=[2,25,75], target=100))
# print(s.twoSum(numbers=[3,24,50,79,88,150,345], target=200))
print(s.twoSum(numbers=[1,2,3,4,4,9,56,90], target=8)) # [4, 5]가 정답


# def do_test():
#     with open(pathlib.Path().cwd() / "010-case", "r") as f:
#         print(s.twoSum(numbers=eval(f.readline()), target=5))  # [13011, 13012]
# execution_time = timeit.timeit(
#     "do_test()",
#     globals=globals(),
#     number=1,
# )
# print(f"quicksort() execution time: {execution_time}")
