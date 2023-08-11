import random

from typing import List


def make_array(
        times: int,
        max: int,
) -> List[int]:
    """
    n만큼의 배열을 최대 max 만큼 생성한다.

    max: 최대 범위
    times: n회 생성
    """
    return [random.randint(1, max) for _ in range(times)]
