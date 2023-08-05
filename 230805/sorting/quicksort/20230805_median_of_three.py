#
# median-of-three 구현
#


import timeit
import cProfile

from typing import List

from utils import make_array


def get_median_of_three(
        nums: List[int],
        lo: int,
        hi: int,
):
    """
    좌, 중간, 우측 값을 사용하여 median을 찾는다
    """
    mid = lo + ((hi - lo) // 2)

    if nums[lo] > nums[mid]:
        nums[lo], nums[mid] = nums[mid], nums[lo]
    if nums[lo] > nums[hi]:
        nums[lo], nums[hi] = nums[hi], nums[lo]
    if nums[mid] > nums[hi]:
        nums[mid], nums[hi] = nums[hi], nums[mid]

    return mid


def partition(
        nums: List[int],
        lo: int,
        hi: int,
        pivot: int,
) -> int:
    """
    획득한 pivot을 가지고, lo, hi가 교차되는 지점까지 swap한다
    """
    pivot_value = nums[pivot]
    nums[pivot], nums[hi] = nums[hi], nums[pivot]
    stored_index = lo

    for idx in range(lo, hi):
        if nums[idx] < pivot_value:
            nums[idx], nums[stored_index] = nums[stored_index], nums[idx]
            stored_index += 1

    nums[stored_index], nums[hi] = nums[hi], nums[stored_index]
    return stored_index


def quicksort(nums: List[int], lo: int, hi: int):
    """
    median-of-3 기법을 이용하여 파티션을 나누고, quicksort를 수행한다.
    """
    if lo < hi:
        pivot = get_median_of_three(nums, lo, hi)

        new_pivot_index = partition(nums, lo, hi, pivot)

        quicksort(nums, lo, new_pivot_index - 1)
        quicksort(nums, new_pivot_index + 1, hi)


a = make_array(7, 100)
quicksort(a, 0, len(a) - 1)
print(a)

# 1. timeit으로 수행시간 테스트. 아래와 같이 실행함:
# execution_time = timeit.timeit(
#     "quicksort(a, 0, len(a) - 1)",
#     globals=globals(),
#     number=1,
# )
# print(f"quicksort() execution time: {execution_time}")

# 2. cProfile로 어떤 구문이 얼마만큼 실행되었는지 프로파일링
#    stdout으로 실행내용이 나옴. 아래와 같이 실행함:
# cProfile.run("quicksort(a, 0, len(a) - 1)")
