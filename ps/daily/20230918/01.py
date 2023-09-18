#
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
#

import bisect
import operator

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat_order = list()
        for idx, row in enumerate(mat):
            very_last_one = bisect.bisect_left(row[::-1], 1)
            mat_order.append((len(row) - very_last_one, idx))

        mat_order = sorted(mat_order, key=operator.itemgetter(0, 1))

        return mat_order


s = Solution()
print(s.kWeakestRows(
    mat=[
        [1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1],
    ], 
    k=3,
))
print(s.kWeakestRows(
    mat=[
        [1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]
    ], 
    k=2,
))
