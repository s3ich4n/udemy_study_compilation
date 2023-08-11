import heapq
import collections

from typing import Optional, Dict, List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        a = heapq.nlargest(k, nums)[-1]

        return a


s = Solution()
s.findKthLargest(nums=[3,2,1,5,6,4], k=2)
s.findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k=4)
