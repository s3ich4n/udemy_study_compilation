from typing import List

from utils import make_array


def get_pivot(A, lo, hi):
    pivot = A[hi]                       # 끝값을 피벗으로 둔다
    i = lo - 1                          # i 값은 lo - 1
    for j in range(lo, hi):             # lo ~ (hi-1) 까지 돌면서...
        if A[j] <= pivot:               # 피벗보다 값이 작다면? (정렬조건임)
            i += 1                      # 좌측으로 값을 정렬하기 위해 i++
            A[i], A[j] = A[j], A[i]     # 값 변경
    A[i + 1], A[hi] = A[hi], A[i + 1]   # 사용한 피벗 값은 맨 왼쪽으로...
    return i + 1


def quicksort(nums: List[int], lo: int, hi: int):
    if lo >= hi or lo < 0:
        return

    pivot = get_pivot(nums, lo, hi)

    quicksort(nums, lo, pivot - 1)
    quicksort(nums, pivot + 1, hi)


a = make_array(5, 100)

quicksort(a, 0, len(a) - 1)
print(a)
