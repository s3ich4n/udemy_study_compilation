import collections
from typing import Optional, Dict, List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 리프노드를 찾는다
        leaves = []
        for idx in range(n):
            if len(graph[idx]) == 1:
                leaves.append(idx)  # 인덱스값만

        # 어쨌거나 갯수가 최대 2개까지 남을 수 있다
        #   단독 하나만 남는 경우
        #   두 개 남는 경우
        while n > 2:
            n -= len(leaves)        # 인덱스만큼 줄이기
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()   # 인접한 값의 리프노드 하나 지우기
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)   # 한개 남았으면 리프노드로 관리

            leaves = new_leaves     # 기존 쫓아간건 필요없으니 "덮어쓰기"

        return leaves


s = Solution()
# print(s.findMinHeightTrees(n=10, edges=[[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]]))
print(s.findMinHeightTrees(n=4, edges=[[1,7],[1,2],[1,3]]))
print(s.findMinHeightTrees(n=6, edges=[[3,0],[3,1],[3,2],[3,4],[5,4]]))
