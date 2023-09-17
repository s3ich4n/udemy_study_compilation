#
# https://leetcode.com/problems/path-with-minimum-effort/
#
#   갈 수 있는 경로는 우측이냐 하단이냐다. (좌상단에서 우하단으로 가니까)
#   그러면 최단길이를 찾기위해... 배웠던 선택지가 여럿 있다
#       1. DFS, 이진 탐색으로 처리


import sys
from typing import List, Set


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        arr = [
            [sys.maxsize for _ in range(len(heights))]
            for _ in range(len(heights[-1]))
        ]

        def dfs(i: int, j: int, effort: int, visited: Set[List[int]]):
            if not (
                0 <= j < len(heights)
                and 0 <= i < len(heights[j])
            ) or (i, j) in visited:
                return

            if arr[i][j] < abs(heights[i][j] - effort):
                return

            max_effort = min(heights[i][j], abs(heights[i][j] - effort))
            arr[i][j] = max_effort

            dfs(i + 1, j, max_effort, visited)
            dfs(i - 1, j, max_effort, visited)
            dfs(i, j + 1, max_effort, visited)
            dfs(i, j - 1, max_effort, visited)

            return

        visited = set()

        if len(heights[-1]) == 1:
            return 0

        dfs(0, 0, heights[0][0], visited)

        return arr[-1][-1]


s = Solution()
# print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))      # 예상 결과: 2
print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))      # 예상 결과: 1
# print(s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))      # 예상 결과: 0
# print(s.minimumEffortPath([[3]]))      # 예상 결과: 0
# print(s.minimumEffortPath([[1,10,6,7,9,10,4,9]]))      # 예상 결과: 9
# print(
#     s.minimumEffortPath(
#         [
#             [4,3,4,10,5,5,9,2],
#             [10,8,2,10,9,7,5,6],
#             [5,8,10,10,10,7,4,2],
#             [5,1,3,1,1,3,1,9],
#             [6,4,10,6,10,9,4,6],
#         ]
#     )
# )     # 예상 결과: 5
