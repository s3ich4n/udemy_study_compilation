import heapq

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        answer = None

        def sort_by_sqrt(arrs: List[List[int]]):
            for x, y in arrs:
                dist = pow(x, 2) + pow(y, 2)
                heapq.heappush(min_heap, (dist, x, y))

        sort_by_sqrt(points)
        
        answer = []

        for _, x, y in heapq.nsmallest(k, min_heap):
            answer.append([x, y])

        return answer


s = Solution()
s.kClosest(points=[[1,3],[-2,2]], k=1)
s.kClosest(points=[[3,3],[5,-1],[-2,4]], k=2)
