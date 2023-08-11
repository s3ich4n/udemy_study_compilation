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

    피벗값을 기준으로 좌측에는 작은 값을, 우측에는 큰 값으로 분할한다.
    """
    pivot_value = nums[pivot]
    # 피벗값 좌측에 작은 값을 두는 연산을 편하게 하기 위해 스왑한다.
    nums[pivot], nums[hi] = nums[hi], nums[pivot]

    # lo 값을 중심으로, 그 보다 작은 값을 왼편에
    # 그 보다 큰 값을 오른편에 두기 위해 stored_index 를 별도로 저장
    stored_index = lo

    for idx in range(lo, hi):
        # 피벗값보다 작으면... 현재 인덱스의 값과 stored_index 위치의 값을 스왑
        if nums[idx] < pivot_value:
            nums[idx], nums[stored_index] = nums[stored_index], nums[idx]
            # stored_index 를 +1 하면서,
            # 작은 값들의 연산 결과에 대한 마지막 인덱스를 기록한다
            stored_index += 1

    # 피벗을 다시 원위치 시켜, 현재 피벗보다 작은값/큰값이 분리되게 완성함
    nums[stored_index], nums[hi] = nums[hi], nums[stored_index]

    # 해당 연산을 마친 인덱스값을 전달
    return stored_index


def quicksort(nums: List[int], lo: int, hi: int):
    """
    median-of-3 기법을 이용하여 파티션을 나누고, quicksort를 수행한다.
    """
    if lo < hi:
        pivot = get_median_of_three(nums, lo, hi)

        new_pivot_index = partition(nums, lo, hi, pivot)

        # partition을 통해 "분할지점"을 찾았으니,
        # 이를 통해 분할 후 `partition()` 을 또 수행하여
        # "분할" 및 "정복"을 수행한다.
        # "결합"은 "분할"을 하는 과정에서 이미 이루어지므로
        # 여기서는 아무 것도 하지 않는다.
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
