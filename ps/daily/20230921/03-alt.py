#
# https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# 각 배열에 대해 중간으로 나누고,
#


from typing import List
# import heapq
import statistics


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(sorted(nums1 + nums2))


s = Solution()
print(s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
