from typing import List


class Solution:
    grid: List[List[str]]

    def num_of_islands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int):
            if i < 0 or i >= len(grid) \
                    or j < 0 or j >= len(grid[0]) \
                    or grid[i][j] != '1':
                return

            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


if __name__ == "__main__":
    q = Solution()

    test1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    test2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    print(q.num_of_islands(test1))
    print(q.num_of_islands(test2))
