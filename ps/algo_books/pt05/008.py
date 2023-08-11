from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        어프로치 (교재)

        1. 피벗을 찾는다. 가장 작은 값을 피벗으로 간주한다.
            문제 조건을 보고 결정. 아래는 문제 조건:
            - nums 배열은 rotate 했을 수도 있는 오름차순 배열임
            - 따라서 오름차순이 되어있지 않다한들 피벗을 찾을 수는 있음
                - 맨 끝이 피벗이면 그냥 이진검색임
        2. 찾은 피벗을 기준으로 이진검색을 수행한다.

        """
        if not nums:
            return -1

        # 최소값이 left에 있으니, 이를 피벗에 저장.
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 찾은 피벗값을 기준으로 이진검색 실시
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1


s = Solution()
print(s.search(nums=[4,5,6,7,0,1,2], target=0))
print(s.search(nums=[4,5,6,7,0,1,2], target=3))
print(s.search(nums=[1], target=0))
