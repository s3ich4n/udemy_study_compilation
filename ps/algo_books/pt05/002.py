import sys

from typing import Optional, List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        result = []

        for x, y in sorted_intervals:
            if not result:
                result.append([x, y])
                continue

            if result[-1][1] >= x:
                if result[-1][0] < x:
                    result[-1] = [result[-1][0], y]
                else:
                    # 반복문을 또 돌려서 최적화해야됨
                    if result[0][0] > x:
                        result = [[x, y]]
                    else:
                        result[-1] = [x, y]
                        result = self.merge(result)

            else:
                result.append([x, y])

        return result


intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]
intervals = [[1,4],[0,4]]
intervals3 = [[1,4],[0,0]]
intervals4 = [[1,4],[0,2],[3,5]]
intervals5 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
intervals6 = [[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]

s = Solution()
# print(s.merge(intervals=intervals))
# print(s.merge(intervals=intervals1))
# print(s.merge(intervals=intervals2))
# print(s.merge(intervals=intervals3))
# print(s.merge(intervals=intervals4))
# print(s.merge(intervals=intervals5))
print(s.merge(intervals=intervals6))
