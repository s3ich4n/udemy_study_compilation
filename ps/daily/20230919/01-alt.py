#
# https://leetcode.com/problems/find-the-duplicate-number/
#


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()    # 생각해보니 이게 훨씬 싸게 치이네?
        for i in nums:
            if i in seen:
                return i
            seen.add(i)


s = Solution()
print(s.findDuplicate(nums=[1,3,4,2,2]))
print(s.findDuplicate(nums=[3,1,3,4,2]))
