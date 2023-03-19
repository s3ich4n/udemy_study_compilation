from typing import List


def solution1(block: List[int]):
    """ 

    한쪽만 반복문을 돌리면 O(n^2)인데, DP 접근을 함께하면 O(n)에 끝낼 수도 있다.

    1. 왼쪽 최대높이를 기역하고있는다.
    2. 중간 높이를 기억하고있는다.
    3. 오른쪽 최대높이 > 왼쪽 최대높이일 때는 쌓여있는 물의 높이를 구한다.

    """
    if len(block) < 3:
        return 0

    left_max = [0 for _ in range(len(block))]
    right_max = [0 for _ in range(len(block))]

    for idx in range(1, len(block)):
        # 왼쪽 최고값은 바로 직전의 값으로 비교해야한다.
        left_max[idx] = max(left_max[idx - 1], block[idx - 1])

    for idx in range(len(block) - 1, -1, -1):
        # 오른쪽 최고값도 이전값의 값으로 비교해야한다.
        left_max[idx] = max(left_max[idx + 1], block[idx + 1])

    trapped = 0

    for idx in range(1, len(block) - 1):
        if min(left_max[idx], right_max[idx]) > block[idx]:
            trapped += min(left_max[idx], right_max[idx]) - block[idx]


test1 = [4, 1, 3, 1, 5]
test2 = [1, 0, 2, 1, 3, 1, 2, 0, 3]
solution1(test1)
solution1(test2)
