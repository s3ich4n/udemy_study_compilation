#
# 초반 어프로치.
# 최소값을 미리 구하고, BFS나 DFS를 하면 될까? 했음
# https://leetcode.com/problems/min-cost-to-connect-all-points/
#


import collections
import sys

from typing import List


Point = collections.namedtuple("Point", ['x', 'y'])


class Solution:
    min_cost = sys.maxsize

    @staticmethod
    def get_cost(p1: Point, p2: Point) -> int:
        """ 두 좌표간 Manhattan distance를 구함

        Args:
            p1 (Point): 좌표 1
            p2 (Point): 좌표 2

        Returns:
            int: manhattan distance 값
        """
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def get_min_position(self, x, y, points):
        xpos = Point(x=points[x][0], y=points[x][1])
        ypos = Point(x=points[y][0], y=points[y][1])
        cur_cost = self.get_cost(xpos, ypos)
        if cur_cost < self.min_cost:
            # print(f"xpos: {xpos}, ypos: {ypos} ... min_cost: {cur_cost}")
            return True, cur_cost
        else:
            return False, -1

    def make_graph(self, points):
        _graph = set()

        if len(points) == 1:
            _graph.add((Point(0, 0), Point(0, 0)))

        else:
            for x in range(len(points)):
                for y in range(0, len(points)):
                    if x == y:
                        continue

                    is_min_position, cur_cost = self.get_min_position(x, y, points)
                    if is_min_position:
                        self.min_cost = cur_cost
                        cur_min_position_x = Point(x=points[x][0], y=points[x][1])
                        cur_min_position_y = Point(x=points[y][0], y=points[y][1])

                print(f"current min cost... xpos: {cur_min_position_x}, ypos: {cur_min_position_y} => {self.min_cost}")
                if ((cur_min_position_y), (cur_min_position_x)) in _graph:
                    pass
                else:
                    _graph.add((cur_min_position_x, cur_min_position_y))
                self.min_cost = sys.maxsize

        return _graph

    def get_answer(self, _graph):
        answer = 0

        for val in _graph:
            answer += self.get_cost(val[0], val[1])

        return answer

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 이런 표현 가능하다!
        
        graph = self.make_graph(points)

        return self.get_answer(graph)


s = Solution()
# print(s.minCostConnectPoints(points=[[3,12],[-4,1],[-2,5]]))
# print(s.minCostConnectPoints(points=[[0,0],[2,2],[3,10],[5,2],[7,0]]))
# print(s.minCostConnectPoints(points=[[0,0]]))
print(s.minCostConnectPoints(points=[[2,-3],[-17,-8],[13,8],[-17,-15]]))    # 53 나와야함
