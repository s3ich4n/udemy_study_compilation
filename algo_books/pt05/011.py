import bisect

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        어프로치 (1) - bisect 활용
        
        1. 매 행마다 bisect를 수행한다
        2. index가 넘어가지 않았는지 확인하며 타깃을 찾았는지 순회한다.

        아마도 O(N log N)?
        - 배열 전부 도니까 N만큼
        - bisect에 log N만큼
        """
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True

        return False


s = Solution()
print(s.searchMatrix(
    matrix=[
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30],
    ],
    target=5,
))
print(s.searchMatrix(
    matrix=[
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30],
    ],
    target=20,
))
