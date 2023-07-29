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

        leaves = sorted(graph.items(), key=lambda item: len(item[1]))

        graph = collections.defaultdict(list, leaves)

        # FIXME
        # 리프노드를 지속적으로 갱신시키는 작업을 어찌해야할지 감이안옴
        # 책에서 제시한 코드는 이해함
        while len(graph) > 2:
            for leaf, connected in leaves:
                # if len(graph[leaf]) == 0:
                #     del graph[leaf]
                #     continue

                linked_leaf = connected.pop()
                graph[linked_leaf].remove(leaf)
                if len(connected) == 0:
                    graph[leaf] = -1

        return list(graph.keys())


s = Solution()
# s.findMinHeightTrees(
#     n=10,
#     edges=[[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]],
# )
# print(s.findMinHeightTrees(n=4, edges=[[1,0],[1,2],[1,3]]))
print(s.findMinHeightTrees(n=6, edges=[[3,0],[3,1],[3,2],[3,4],[5,4]]))
