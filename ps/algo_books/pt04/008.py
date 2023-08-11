
import collections
import heapq
import math

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        _graph = [[] for _ in range(n)]

        for u, v, w in flights:
            _graph[u].append((v, w))

        Q = [(0, src, k + 1)]

        # k + 1에 대하여
        #   최대 이동거리만큼 만들어 놓기 때문에 더 만들어봐야 의미 X (예외처리 때문에 + 2)
        dist = [[math.inf] * (k + 1) for _ in range(n)]

        while Q:
            d, u, stops = heapq.heappop(Q)

            if u == dst:
                return d

            if stops > 0:
                for v, w in _graph[u]:
                    newDist = d + w
                    if newDist < dist[v][stops - 1]:
                        dist[v][stops - 1] = newDist
                        heapq.heappush(Q, (newDist, v, stops - 1))

        return -1

s = Solution()

# route = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]]
route = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# route = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]

print(s.findCheapestPrice(n=4, flights=route, src=0, dst=3, k=1))
