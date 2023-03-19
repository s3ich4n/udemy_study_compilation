from typing import List


def median_of_medians(
    nums: List[int],
    k: int,
):
    """ Median of Medians 알고리즘 구현

    nums: integer 값이 들어간 배열
    k: k - 1번째 값을 표현
    """

    # 5개의 청크단위로 기존 배열을 넘김
    chunks = [nums[i:i+5] for i in range(0, len(nums), 5)]

    # 정렬은 그냥 sorted()를 씀
    # 정확한 중앙값을 찾는 것이 아니라
    # 최대한 가까운 근사치를 찾는 것임에 유의!
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]
    pivot_value = sorted(medians)[len(medians)//2]

    left_array = [n for n in nums if n < pivot_value]
    right_array = [n for n in nums if n > pivot_value]

    # selection phase
    pivot_index = len(left_array)
    if k < pivot_index:
        # 좌측 배열을 살펴본다
        return median_of_medians(left_array, k)
    elif k > pivot_index:
        # 우측 배열을 살펴본다
        return median_of_medians(right_array, k - len(left_array) - 1)

    return nums[k]


def select(
    nums,
    k,
):
    return median_of_medians(nums, k - 1)


# x = [1, -2, 5, 8, 7, 6, 10, 4, 18, 2, 3, -4, 55, 0, 11]  # noqa
x = [1, -5, 0, 10, 15, 20, 3, -1]
print(select(x, 1))
print(select(x, 2))
print(select(x, 3))
print(select(x, 4))
