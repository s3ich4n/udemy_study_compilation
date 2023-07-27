#
# 예시는 이거로:
#   https://www.youtube.com/watch?v=tZu4x5825LI
#

import collections
import heapq
import sys
from typing import List

INFINITY = -sys.maxsize

# ebs_single_route = [
#     [1, 2, 5],
#     [1, 3, 10],
#     [1, 4, 9],
#     # [2, 1, 5],
#     [2, 3, 3],
#     [2, 6, 11],
#     [3, 1, 10],
#     # [3, 2, 3],
#     [3, 4, 7],
#     [3, 5, 3],
#     [3, 6, 10],
#     # [4, 1, 9],
#     # [4, 3, 7],
#     [4, 6, 7],
#     [4, 7, 12],
#     # [5, 3, 3],
#     [5, 6, 4],
#     # [6, 2, 11],
#     # [6, 3, 10],
#     # [6, 4, 7],
#     # [6, 5, 4],
#     [6, 7, 2],
#     # [7, 4, 12],
#     # [7, 6, 2],
# ]

# 루트가 중복되어도 상관없다!!!!!!!
whatif_ebs_single_route = [
    [1, 2, 5],
    [1, 3, 10],
    [1, 4, 9],
    [2, 1, 5],
    [2, 3, 3],
    [2, 6, 11],
    [3, 1, 10],
    [3, 2, 3],
    [3, 4, 7],
    [3, 5, 3],
    [3, 6, 10],
    [4, 1, 9],
    [4, 3, 7],
    [4, 6, 7],
    [4, 7, 12],
    [5, 3, 3],
    [5, 6, 4],
    [6, 2, 11],
    [6, 3, 10],
    [6, 4, 7],
    [6, 5, 4],
    [6, 7, 2],
    [7, 4, 12],
    [7, 6, 2],
]

nodes = 7
source = 1

# graph = [
#     [3, 1, 5], 
#     [3, 2, 2],
#     [2, 1, 2], 
#     [3, 4, 1],
#     [5, 6, 1],
#     [6, 7, 1],
#     [7, 8, 1],
#     [8, 1, 1],
# ]
# nodes = 8
# source = 3


# GRAPH = [
#     [1, 2, ]
# ]


def solution(graph: List[int], nodes: int, source: int):
    _graph = collections.defaultdict(list)

    # 시작, 도착 그리고 탐색시간
    for u, v, w in graph:
        _graph[u].append((v, w))

    Q = [(0, source)]
    heapq.heapify(Q)
    dist = collections.defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:                    # 아무것도 없으면 push 시작
            dist[node] = time                   # 이 경우에만 heap에 push
            for v, w in _graph[node]:           # 없는 노드의 도착, 탐색시간을 쫓아가며 연산
                alt = time + w                  # 누적된 탐색시간을 계속 더함 (alt는 원본에 그렇게 써져있는 값)
                heapq.heappush(Q, (alt, v))

    if len(dist) == nodes:                      # 전체 노드 개수만큼 모두 dist에 있다면 최단경로를 구한것
        return max(dist.values())

    return -1


# print(solution(graph, nodes, source))
print(solution(whatif_ebs_single_route, nodes, source))
