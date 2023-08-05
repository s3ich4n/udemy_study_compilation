from typing import List

from utils import make_array


def get_pivot(A, lo, hi):
    """
    오름차순 정렬을 위해 피벗값을 가지고 정렬을 실시
    """
    pivot = A[lo]

    i = lo - 1                          # 좌측 인덱스
    j = hi + 1                          # 우측 인덱스

    while True:
        j -= 1
        while A[j] > pivot:            # pivot 보다 큰 경우
            j -= 1
        i += 1
        while A[i] < pivot:            # pivot 보다 작은경우
            i += 1

        if i < j:
            A[i], A[j] = A[j], A[i]

        else:                           # i, j가 겹치면 리턴함
            return j


def quicksort(nums: List[int], lo: int, hi: int):
    if lo >= 0 and hi >= 0 and lo < hi:
        # 피벗값을 구한 후
        pivot = get_pivot(nums, lo, hi)

        # 해당 피벗으로 분할정복 실시 (퀵소트 사용)
        quicksort(nums, lo, pivot)
        quicksort(nums, pivot + 1, hi)


a = make_array(5, 100)

quicksort(a, 0, len(a) - 1)
print(a)
