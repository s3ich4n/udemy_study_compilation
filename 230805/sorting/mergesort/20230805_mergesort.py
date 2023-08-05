import cProfile
import timeit

from typing import List

from utils import make_array


def compare(left, right):
    result = []
    i = j = 0

    while True:
        if len(left) == i and len(right) == j:
            break
        else:
            if len(left) == i:
                result.append(right[j])
                j += 1
            elif len(right) == j:
                result.append(left[i])
                i += 1

            elif left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    return result


def mergesort(nums: List[int], lo: int, hi: int):
    total_length = len(nums)

    if total_length < 2:
        return nums

    mid = lo + ((hi - lo) // 2)

    left = mergesort(nums[:mid], 0, mid)
    right = mergesort(nums[mid:], mid, total_length)

    return compare(left, right)


a = make_array(1_000_000, 1_000_000_000)
# x = mergesort(a, 0, len(a))
# print(x)


# 1. timeit으로 수행시간 테스트. 아래와 같이 실행함:
# execution_time = timeit.timeit(
#     "mergesort(a, 0, len(a))",
#     globals=globals(),
#     number=1,
# )
# print(f"quicksort() execution time: {execution_time}")

# 2. cProfile로 어떤 구문이 얼마만큼 실행되었는지 프로파일링
#    stdout으로 실행내용이 나옴. 아래와 같이 실행함:
cProfile.run("mergesort(a, 0, len(a))")
