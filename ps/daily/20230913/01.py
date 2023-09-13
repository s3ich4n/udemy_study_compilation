#
# https://leetcode.com/problems/candy/
#


from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 모든 아이는 적어도 하나의 사탕을 받아야함
        # 이웃보다는 많이 받아야됨 (양쪽보다 rating이 높으면 +1)
        # 양쪽을 어떻게 살펴봐야하지? 이거 DP인가?
        # -> 그리디로 먼저 접근하자. 당장 최적의 해가 안 보인다.
        result = [1 for _ in range(len(ratings))]

        for left in range(1, len(ratings)):
            if ratings[left - 1] < ratings[left]:
                result[left] = result[left - 1] + 1

        for right in range(len(ratings) - 2, -1, -1):
            if ratings[right] > ratings[right + 1]:
                # This ensures that both neighboring conditions are checked and satisfied.
                result[right] = max(result[right + 1] + 1, result[right])

        return sum(result)


s = Solution()
print(s.candy(ratings=[1,0,2]))     # 5
print(s.candy(ratings=[1,2,2]))     # 4
print(s.candy(ratings=[1,3,2,2,1]))     # 7
print(s.candy(ratings=[1,2,87,87,87,2,1]))     # 13
