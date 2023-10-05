#
# https://leetcode.com/problems/majority-element-ii/
#
# 어프로치 #3
#   Misra-Gries heavy-hitters algorithm으로 접근해보자.
#   https://en.wikipedia.org/wiki/Misra%E2%80%93Gries_summary
#
#   이 알고리즘 또한 스트리밍 알고리즘의 일부이다.
#   이들은 frequent elements를 구하는 접근방법이다.
#   https://en.wikipedia.org/wiki/Streaming_algorithm
#


import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int], k: int) -> List[int]:
        K = k
        mg_counts = collections.defaultdict(int)

        for token in nums:
            if token in mg_counts:
                mg_counts[token] += 1

            elif len(mg_counts.keys()) < K:
                mg_counts[token] += 1

            else:
                for key in list(mg_counts.keys()):
                    mg_counts[key] -= 1
                    if mg_counts[key] == 0:
                        del mg_counts[key]

        return [x for x in mg_counts.keys()]


s = Solution()
# print(s.majorityElement(nums=[3,2,3]))
# print(s.majorityElement(nums=[1]))
# print(s.majorityElement(nums=[1,2]))
# print(s.majorityElement(nums=[32,12,14,32,7,12,32,7,6,12,4], k=3))
# print(s.majorityElement(nums=[1,4,5,4,4,5,4,4], k=5))
print(s.majorityElement(nums=[2,3,1,1,4,4,4,4,4,4,4,4,4,4,2,2,2,2,21,1,3], k=3))
# print(s.majorityElement(nums=[1,2,3,4,5,1,2,3,3,3]))
