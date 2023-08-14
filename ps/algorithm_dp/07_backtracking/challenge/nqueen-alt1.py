#
# https://leetcode.com/problems/n-queens/
#
import copy
from typing import List


def print_current_tile(tiles):
    print("\n")
    for tile_x in tiles:
        for tile_y in tile_x:
            print(f"{tile_y:2}", end="")
        print("")


class Solution:
    def __init__(self, n):
        self.result = []
        self.tile = [["." for _ in range(0, n)] for _ in range(0, n)]

    @staticmethod
    def discriminate(tile, x, y) -> bool:
        print(f"{x}, {y} 판별 시작.")
        print_current_tile(tile)
        triggered = False

        # x 좌표가 겹치는가? (0, 0), (1, 0), (2, 0), ... (n, 0)
        x_size = (x for x in range(len(tile)))
        for _x in x_size:
            if tile[_x][y] == "Q":
                triggered = True
                break

        # y 좌표가 겹치는가? (0, 0), (0, 1), (0, 2), ... (0, n)
        y_size = (y for y in range(len(tile)))
        for _y in y_size:
            if tile[x][_y] == "Q":
                triggered = True
                break

        # x, y를 -1 계속하면서 둘 중 하나가 0값이 되면?
        # abs(x2-x1) == abs(y2-y1) 이면?
        x_size, y_size = x, y
        while x_size > 0 and y_size > 0:
            if tile[x_size - 1][y_size - 1] == "Q":
                triggered = True
                break
            else:
                x_size -= 1
                y_size -= 1

        x_size, y_size = x, y
        while x_size > 0 and y_size < len(tile) - 1:
            if tile[x_size - 1][y_size + 1] == "Q":
                triggered = True
                break
            else:
                x_size -= 1
                y_size += 1

        if triggered:
            return False
        else:
            tile[x][y] = "Q"
            print_current_tile(tile)
            return True

    def dfs(self, _times: int, n: int, _x: int, _y: int):
        if _x >= n or _y >= n:
            return
        else:
            if self.discriminate(self.tile, _x, _y):
                if _times == 0:
                    self.result.append(copy.deepcopy(self.tile))
                    self.tile[_x][_y] = "."
                    return
                else:
                    self.dfs(_times - 1, n, _x + 1, 0)
                    print(f"tile[{_x}][{_y}] 원상복구.")
                    self.tile[_x][_y] = "."
                    return
            else:
                self.dfs(_times, n, _x, _y + 1)
                print(f"tile[{_x}][{_y}] 원상복구.")
                self.tile[_x][_y] = "."

    def refine_result(self):
        answer = []

        for tiles in self.result:
            new = []
            for tile in tiles:
                new.append("".join(tile))
            answer.append(new)
            new = []

        return answer

    def solveNQueens(self, n: int) -> List[List[str]]:
        for idx in range(n):
            self.dfs(n - 1, n, 0, idx)
            self.tile[0][idx] = "."

        answer = self.refine_result()

        return answer

    def print_result(self):
        print("--결과--")

        for idx, tiles in enumerate(self.result):
            print(f"{idx}회차")
            for tile_x in tiles:
                for tile_y in tile_x:
                    print(f"{tile_y} ", end="")
                print("")


s = Solution(5)
s.solveNQueens(5)
s.print_result()
