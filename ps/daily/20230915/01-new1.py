#
# 작업예정
# https://leetcode.com/problems/min-cost-to-connect-all-points/
#

#
# 사용된 테크닉
#   최소 신장 트리
#       크루스칼 알고리즘
#   Union Find(서로소)
#

import collections
import sys

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 최소신장트리를 구할 값들을 미리 구한다 (가중치 계산 포함)
        # Union-Find 를 구현한다

        tree = []

        for x in range(len(points)):
            for y in range(len(points)):
                if x == y:
                    pass
                else:
                    cost = abs(points[][] - points[][]) + abs(points[][] - points[][])



s = Solution()
# print(s.minCostConnectPoints(points=[[3,12],[-4,1],[-2,5]]))
# print(s.minCostConnectPoints(points=[[0,0],[2,2],[3,10],[5,2],[7,0]]))
# print(s.minCostConnectPoints(points=[[0,0]]))
print(s.minCostConnectPoints(points=[[2,-3],[-17,-8],[13,8],[-17,-15]]))    # 53 나와야함
