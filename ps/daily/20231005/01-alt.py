#
# https://leetcode.com/problems/majority-element-ii/
#
# 어프로치 #2
#   Boyer-Moore voting algorithm 을 먼저 학습하자
#
#   이 알고리즘은 스트리밍 알고리즘의 일부이다.
#   이들은 frequent elements를 구하는 접근방법이다.
#   https://en.wikipedia.org/wiki/Streaming_algorithm
#
#


import collections
from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         """
#         이러면 "가장 최고빈도의 값"을 갖고오는 셈이다.

#         MAJORITY 알고리즘의 구현체.
#         """
#         majority = counter = 0

#         for number in nums:
#             if counter == 0:
#                 majority = number
#                 counter = 1
#             elif majority == number:
#                 counter += 1
#             else:
#                 counter -= 1

#         return majority


# s = Solution()
# print(s.majorityElement(nums=[3,2,3]))
# print(s.majorityElement(nums=[1]))
# print(s.majorityElement(nums=[1,2]))
# print(s.majorityElement(nums=[2,3,1,1,4,4,4,4,4,4,4,4,4,4,2,2,2,2,21,1,3]))
# print(s.majorityElement(nums=[2,3,1,1,4,4,4,4,4,4,4,4,4,4,2,2,2,2,21,1,3,3,1]))
# print(s.majorityElement(nums=[1,2,3,4,5,1,2,3,3,3]))


# -----------------------------------------------------------------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """ 변수 두 개와 정답 담을 리스트만 사용해서 최다빈도를 구하는 알고리즘

        cf. https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

        Args:
            nums (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        K = len(nums) // 3

        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1

        return [n for n in (candidate1, candidate2) if nums.count(n) > K]

        # 위 코드는 아래 내용을 한줄로 압축한 것이다!
        # answer = []
        # for n in (candidate1, candidate2):
        #     if nums.count(n) > K:
        #         answer.append(n)
        # return answer


s = Solution()
# print(s.majorityElement(nums=[3,2,3]))
# print(s.majorityElement(nums=[1]))
# print(s.majorityElement(nums=[1,2]))
print(s.majorityElement(nums=[2,3,1,1,4,4,4,4,4,4,4,4,4,4,2,2,2,2,21,1,3]))
# print(s.majorityElement(nums=[1,2,3,4,5,1,2,3,3,3]))
