#
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
#


import collections

from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []
        person_belong_to = collections.defaultdict(list)

        for idx, x in enumerate(groupSizes):
            person_belong_to[x].append(idx)

        for k, v in person_belong_to.items():
            max_len = k
            temp = []
            for data in v:
                if len(temp) == max_len:
                    answer.append(temp)
                    temp = []
                temp.append(data)
            answer.append(temp)

        return answer


s = Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))
print(s.groupThePeople([2,1,3,3,3,2]))
