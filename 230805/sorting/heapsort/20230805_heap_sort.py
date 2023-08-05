import cProfile
import timeit

import heapq

from typing import List

from utils import make_array


def heapsort(nums: List[int]):
    heapq.heapify(nums)

    return


# a = make_array(1_000_000, 1_000_000_000)
a = make_array(11, 100)
heapsort(a)


# 1. timeit으로 수행시간 테스트. 아래와 같이 실행함:
# execution_time = timeit.timeit(
#     "heapsort(a)",
#     globals=globals(),
#     number=1,
# )
# print(f"quicksort() execution time: {execution_time}")

# 2. cProfile로 어떤 구문이 얼마만큼 실행되었는지 프로파일링
#    stdout으로 실행내용이 나옴. 아래와 같이 실행함:
# cProfile.run("heapsort(a)")
