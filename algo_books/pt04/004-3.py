from typing import List


class Solution:
    def combination_sum(
            self,
            candidates: List[int],
            target: int,
    ) -> List[List[int]]:
        results = []

        def dfs(elements: List[int], target: int, index: int = 0):
            if 0 > target:
                return

            if 0 == target:
                results.append(elements[:])
                return

            for i in range(index, len(candidates)):
                dfs(elements + [candidates[i]], target - candidates[i], i)

        dfs([], target)
        return results


if __name__ == "__main__":
    q = Solution()

    print(q.combination_sum(candidates=[2, 3, 6, 7], target=7))
