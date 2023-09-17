#
# https://leetcode.com/problems/path-with-minimum-effort/
#
#   갈 수 있는 경로는 우측이냐 하단이냐다. (좌상단에서 우하단으로 가니까)
#   그러면 최단길이를 찾기위해... 배웠던 선택지가 여럿 있다
#       2. 다익스트라 알고리즘, heapq를 써서 처리


import heapq
import sys

from typing import List


class Solution:
    @staticmethod
    def is_valid(heights, next_pos):
        dx, dy = next_pos
        if not (0 <= dx < len(heights) and 0 <= dy < len(heights[0])):
            return False
        return True

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        arr = [
            [sys.maxsize for _ in range(len(heights[0]))]
            for _ in range(len(heights))
        ]
        arr[0][0] = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        destination = (len(heights) - 1, len(heights[0]) - 1)
        candidates = [(0, 0, 0)]
        # visited = set()

        while candidates:
            effort, x, y = heapq.heappop(candidates)
            # visited.add((x, y))

            if (x, y) == destination:
                return effort

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if self.is_valid(heights, (nx, ny)) and (nx, ny):
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))

                    if new_effort < arr[nx][ny]:
                        arr[nx][ny] = new_effort
                        heapq.heappush(candidates, (new_effort, nx, ny))


s = Solution()
# print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))      # 예상 결과: 2
# print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))      # 예상 결과: 1
# print(s.minimumEffortPath([[3]]))      # 예상 결과: 0
# print(s.minimumEffortPath([[1,10,6,7,9,10,4,9]]))      # 예상 결과: 9
# print(s.minimumEffortPath(
#     [
#         [1,2,1,1,1],
#         [1,2,1,2,1],
#         [1,2,1,2,1],
#         [1,2,1,2,1],
#         [1,1,1,2,1],
#     ]
# ))      # 예상 결과: 0
# print(s.minimumEffortPath(
#         [
#             [4,3,4,10,5,5,9,2],
#             [10,8,2,10,9,7,5,6],
#             [5,8,10,10,10,7,4,2],
#             [5,1,3,1,1,3,1,9],
#             [6,4,10,6,10,9,4,6],
#         ]
# ))     # 예상 결과: 5
print(s.minimumEffortPath(
    [[3],[3],[7],[2],[9],[9],[3],[7],[10]]
))