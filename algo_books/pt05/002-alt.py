import collections

from typing import Optional, List


coord = collections.namedtuple('Coord', ['x', 'y'])


class Solution:
    # 교재상의 풀이가 안돼서 새로 구함
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        for i in sorted(intervals, key=lambda x: x[1]):
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result += [i]

        return result


intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]
intervals = [[1,4],[0,4]]
intervals3 = [[1,4],[0,0]]
intervals4 = [[1,4],[0,2],[3,5]]
intervals5 = [[2,3],[4,5],[6,7],[8,9],[1,10]]

s = Solution()
# print(s.merge(intervals=intervals))
# print(s.merge(intervals=intervals1))
# print(s.merge(intervals=intervals2))
# print(s.merge(intervals=intervals3))
# print(s.merge(intervals=intervals4))
print(s.merge(intervals=intervals5))
