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
    def is_valid(heights, next_pos, current):
        x, y = current
        dx, dy = next_pos
        if not (0 <= dy < len(heights) and 0 <= dx < len(heights[y])):
            return False

        # y값이 먼저 커지고(inner for loop), x값은 나중에 커진다(outer for loop).
        # 즉, get_neighbors에서 계산하는 식으로 좌표값 내 값을 비교하려면, 이렇게 비교한다.
        # if heights[dy][dx] > heights[y][x]:
        #     return False

        return True

    def get_neighbors(self, heights, current):
        """ 사방으로 돌아다니면서 유효한 길인지 확인한다.

        상하좌우만 돌아다니도록 조절한다

        Args:
            heights (_type_): _description_
            current (_type_): _description_
        """
        x, y = current
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # 상하좌우만 돌아다닌다
                if (dx == 0 and dy == 0) or (abs(dx) + abs(dy) == 2):
                    continue
                position = x + dx, y + dy
                if self.is_valid(heights, position, current):
                    yield position

    def get_efforts(self, heights, current, neighbor) -> int:
        # y가 outer고 x가 inner이기 때문
        return abs(heights[neighbor[1]][neighbor[0]] - heights[current[1]][current[0]])

    def get_paths(self, tentative, positions, through):
        path = tentative[through] + [through]
        for position in positions:
            if position in tentative and len(tentative[position]) <= len(path):
                continue
            yield position, path

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        origin, destination = (0, 0), (len(heights[-1]) - 1, len(heights) - 1)
        tentative = {origin: []}
        candidates = [(1, origin)]
        certain = set()

        if len(heights[-1]) == 1:
            return 0

        while destination not in certain and len(candidates) > 0:
            prev_effort, current = heapq.heappop(candidates)
            if current in certain:
                continue

            certain.add(current)
            neighbors = set(self.get_neighbors(heights, current)) - certain
            less_effort = self.get_paths(tentative, neighbors, current)
            for neighbor, path in less_effort:
                current_effort = self.get_efforts(heights, current, neighbor)
                if abs(current_effort - prev_effort) == 1:
                    tentative[neighbor] = path
                    heapq.heappush(candidates, (1, neighbor))
                
                else:
                    if prev_effort < abs(current_effort - prev_effort):
                        pass
                    else:
                        tentative[neighbor] = path
                        heapq.heappush(candidates, (max(prev_effort, current_effort), neighbor))

        if destination in tentative:
            path = tentative[destination] + [destination]

            answer = 1
            idx = 1
            while idx < len(path) - 1:
                answer = max(answer, self.get_efforts(heights, path[idx - 1], path[idx]))
                idx += 1

            return answer

        else:
            return 0


s = Solution()
# print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))      # 예상 결과: 2
# print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))      # 예상 결과: 1
# print(s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))      # 예상 결과: 0
# print(s.minimumEffortPath([[3]]))      # 예상 결과: 0
# print(s.minimumEffortPath([[1,10,6,7,9,10,4,9]]))      # 예상 결과: 9
print(
    s.minimumEffortPath(
        [
            [4,3,4,10,5,5,9,2],
            [10,8,2,10,9,7,5,6],
            [5,8,10,10,10,7,4,2],
            [5,1,3,1,1,3,1,9],
            [6,4,10,6,10,9,4,6],
        ]
    )
)     # 예상 결과: 5
