#
# https://leetcode.com/problems/majority-element-ii/
#
# 어프로치 #1
#   defaultdict로 세고 majority_floor로 그냥 판단하면?
#   그런데 파이썬 라이브러리들을 적극 사용하면?
#


import collections
from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         majority_floor = len(nums) // 3
#         data = collections.defaultdict(int)
#         answer = []
#
#         for num in nums:
#             data[num] += 1
#
#         for k, v in data.items():
#             if v > majority_floor:
#                 answer.append(k)
#
#         return answer


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        처음 코드를 더 간단하게 다듬은 버전
        """
        K = len(nums) // 3
        L = collections.Counter(nums)
        answer = []
        for element, count in L.items():
            if count > K:
                answer.append(element)

        return answer


s = Solution()
print(s.majorityElement(nums=[3,2,3]))
print(s.majorityElement(nums=[1]))
print(s.majorityElement(nums=[1,2]))
