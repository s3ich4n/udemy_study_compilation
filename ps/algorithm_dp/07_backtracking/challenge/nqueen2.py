#
# https://leetcode.com/problems/n-queens/
#
import collections
import copy
from typing import List


class Solution:
    @staticmethod
    def is_impossible(tile, x, y) -> bool:
        if tile[x] == y or tile[y] == x or abs(x - y) == abs(y - x):
            return True

    def dfs(self, tile, x, y):
        if tile[x] == -1:
            tile[x] = y
            self.dfs(tile, x + 1, y)

        else:
            if self.is_impossible(tile, x, y):
                # 모든 경우가 안 되는 케이스를 감지할 때
                # x, y를 '.' 으로 바꿔야된다
                # tile[x] = -1
                self.dfs(tile, x, y + 1)
            #
            # else:
            #     self.dfs(tile, x + 1, y)

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        tile = collections.defaultdict(int)

        for x in range(n):
            tile[x] = -1

        self.dfs(tile, 0, 0)

        return result

    def print_result(self):
        for tiles in self.result:
            for tile_x in tiles:
                for tile_y in tile_x:
                    print(f"{self.tile[tile_x][tile_y]}")


s = Solution()
s.solveNQueens(4)
s.print_result()
