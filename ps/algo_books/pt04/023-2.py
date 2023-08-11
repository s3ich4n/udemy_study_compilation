import heapq
import collections

from typing import Optional, Dict, List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = []
        for idx in nums:
            heapq.heappush(data, -idx)

        for _ in range(1, k):
            heapq.heappop(data)

        return -heapq.heappop(data)
     
     
        # heapq.heapify(nums)
        # a = heapq.nlargest(k, data)[-1]

        # return a


s = Solution()
print(s.findKthLargest(nums=[3,2,1,5,6,4], k=2))
print(s.findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k=4))
