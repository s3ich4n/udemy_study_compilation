# 0, 1, 2로 정리하기...
from typing import List


def solution(
    flags: List[int],
    mid: int = 1,
):
    """ mid 값인 피벗을 중심으로 영란국 국기 색을 만드는 알고리즘을 만든다.

    i 값은 최소값을 쫓아간다
    j 값은 iteration하는 포인터값 (현재 조회중인 값을 가리킴)
    k 값은 최대값을 쫓아간다

    """
    i = 0
    j = 0
    k = len(flags) - 1

    while j <= k:
        if flags[j] < mid:
            flags[i], flags[j] = flags[j], flags[i]
            i += 1
            j += 1
        elif flags[j] > mid:
            flags[j], flags[k] = flags[k], flags[j]
            k -= 1
        else:
            j += 1


test1 = [0, 1, 2, 1, 2, 0, 0]
solution(test1)
