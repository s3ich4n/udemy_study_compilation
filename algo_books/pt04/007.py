
import collections
import heapq

from typing import List


def solution(graph: List[int], nodes: int, source: int):
    _graph = collections.defaultdict(list)

    # 시작, 도착 그리고 탐색시간
    for u, v, w in graph:
        _graph[u].append((v, w))                # heap의 우선순위가 어떻게 판별되는지 알아보기

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


graph = [
    [3, 1, 5], 
    [3, 2, 2],
    [2, 1, 2], 
    [3, 4, 1],
    [5, 6, 1],
    [6, 7, 1],
    [7, 8, 1],
    [8, 1, 1],
]

print(solution(graph, nodes=8, source=3))  # 최단거리로 가면 모든 노드에 닿는 시간보다 길어져서 안됨
