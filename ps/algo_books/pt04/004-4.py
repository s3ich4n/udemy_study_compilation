from typing import List


class Solution:
    def subsets(
            self,
            nums: List[int],
    ) -> List[List[int]]:
        results = []

        def dfs(elements: List[int], index: int = 0):
            results.append(elements[:])

            for idx in range(index, len(nums)):
                dfs(elements + [nums[idx]], idx + 1)

        dfs([], 0)
        return results


if __name__ == "__main__":
    q = Solution()

    print(q.subsets(nums=[1, 2, 3]))
