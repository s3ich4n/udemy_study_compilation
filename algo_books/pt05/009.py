import bisect

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        어프로치 (1)
        1. 한쪽은 순서대로 탐색, 다른 한 쪽은 정렬 후 이진검색으로 값 찾기

        """
        answer = set()
        nums2.sort()

        for idx in nums1:
            index = bisect.bisect_left(nums2, idx)

            if index >= len(nums2) or nums2[index] != idx:
                continue

            answer.add(idx)

        return answer


s = Solution()
# print(s.intersection(nums1=[1,2,2,1], nums2=[2,2]))
print(s.intersection(nums1=[4,9,5], nums2=[9,4,9,8,4]))
