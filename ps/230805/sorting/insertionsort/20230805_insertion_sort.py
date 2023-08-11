import cProfile
import timeit

from typing import List

from utils import make_array


def insertionsort(nums: List[int]):
    i = 0
    nums_length = len(nums)

    while i < nums_length:
        for x in range(i, 0, -1):
            if nums[x] <= nums[x - 1]:
                nums[x], nums[x - 1] = nums[x - 1], nums[x]
            else:
                continue

        i += 1


a = make_array(10000, 100000)
# insertionsort(a)
# print(a)


# 1. timeit으로 수행시간 테스트. 아래와 같이 실행함:
# a = make_array(10000, 100000)
execution_time = timeit.timeit(
    "insertionsort(a)",
    globals=globals(),
    number=1,
)
print(f"quicksort() execution time: {execution_time}")

# 2. cProfile로 어떤 구문이 얼마만큼 실행되었는지 프로파일링
#    stdout으로 실행내용이 나옴. 아래와 같이 실행함:
# cProfile.run("insertionsort(a)")
