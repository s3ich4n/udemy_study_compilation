#
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# 이 풀이에서 사용된 테크닉
#   최소 신장 트리
#       프림 알고리즘
#   BFS
#   heapq
#


import collections
import heapq

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 사이클 없이 트리를 만드는게 목표임
        N = len(points)

        # i: [cost, node] 를 담는 리스트
        adj = {i: [] for i in range(N)}

        # 처음엔 모든 경로가 죄다 그려져있을것임
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # 힙을 동일노드를 추가하지 않도록 함 (visited, set으로)
        #   visited갯수가 points 길이와 같으면 탈출한다. 5개 다 들렀다는 뜻
        #   frontier (minheap) 으로 갈 수 있는 경로를 랜덤선택이 아니라 minheap 에 넣고 정하는 것으로 보임
        answer = 0
        visited = set()
        heap = [[0, 0]]    # [cost, point]
        while len(visited) < N:
            cost, i = heapq.heappop(heap)

            if i in visited:
                continue

            answer += cost
            visited.add(i)

            for cost, neighbor in adj[i]:
                if neighbor not in visited:
                    heapq.heappush(heap, [cost, neighbor])

        return answer



s = Solution()
# print(s.minCostConnectPoints(points=[[3,12],[-4,1],[-2,5]]))
# print(s.minCostConnectPoints(points=[[0,0],[2,2],[3,10],[5,2],[7,0]]))
# print(s.minCostConnectPoints(points=[[0,0]]))
print(s.minCostConnectPoints(points=[[2,-3],[-17,-8],[13,8],[-17,-15]]))    # 53 나와야함
