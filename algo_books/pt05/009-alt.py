from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        어프로치 (2)
        1. 정렬 후 투포인터 (작업중)

        """
        result = set()
        nums1.sort()
        nums2.sort()

        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result


s = Solution()
# s.intersection(nums1=[1,2,2,1], nums2=[2,2])
# s.intersection(nums1=[4,9,5], nums2=[9,4,9,8,4])
s.intersection(nums1=[1], nums2=[1])
