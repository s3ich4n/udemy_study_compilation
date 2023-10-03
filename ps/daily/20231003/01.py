#
# https://leetcode.com/problems/number-of-good-pairs/
#


from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    answer += 1

        return answer


s = Solution()
print(s.numIdenticalPairs(nums=[1,2,3,1,1,3]))  # 4
print(s.numIdenticalPairs(nums=[1,1,1,1]))      # 6
print(s.numIdenticalPairs(nums=[1,2,3]))        # 0
