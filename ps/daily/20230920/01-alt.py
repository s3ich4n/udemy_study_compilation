#
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
#
# 어프로치 #2
#   반대로 생각하기!
#   최대 subarray를 찾는 방향으로. → 그리디한 접근 가능
#
# maximum subarray? 어디서 어떻게?
#   중앙에서 시작해서 가나?
#   좌로부터 시작해서 슬라이딩 윈도우를 꾸려본다
#
# 어프로치 #2 revisited
#   https://www.youtube.com/watch?v=xumn16n7njs
#   이거보고 풀기
#


from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        answer_table = []
        slow, fast = 0, 0
        answer = 0
        counter = 0

        if len(nums) == 1:
            if nums[0] != x:
                return -1
            else:
                return x

        while fast != len(nums):
            if answer + nums[fast] == x:
                counter += 1
                return counter

            elif answer + nums[fast] < x:
                answer_table.append(nums[fast])
                answer += nums[fast]
                fast += 1

            else:
                counter += 1
                fast += 1

        while slow != len(answer_table):
            if answer - nums[slow] == x:
                # counter -= 1
                return counter
            
            elif answer - nums[slow] > x:
                counter -= 1
                answer -= nums[slow]
                slow += 1

            else:
                slow += 1


s = Solution()
print(s.minOperations(nums=[1,1,4,2,3], x=5))          # 정답: 2
# print(s.minOperations(nums=[5,6,7,8,9], x=4))          # 정답: -1
# print(s.minOperations(nums=[3,2,20,1,1,3], x=10))      # 정답: 5
# print(s.minOperations(nums=[1,1], x=3))      # 정답: 5
# print(s.minOperations(nums=[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], x=134365))      # 정답: 16
# print(s.minOperations(
#     nums=[5207,5594,477,6938,8010,7606,2356,6349,3970,751,5997,6114,9903,3859,6900,7722,2378,1996,8902,228,4461,90,7321,7893,4879,9987,1146,8177,1073,7254,5088,402,4266,6443,3084,1403,5357,2565,3470,3639,9468,8932,3119,5839,8008,2712,2735,825,4236,3703,2711,530,9630,1521,2174,5027,4833,3483,445,8300,3194,8784,279,3097,1491,9864,4992,6164,2043,5364,9192,9649,9944,7230,7224,585,3722,5628,4833,8379,3967,5649,2554,5828,4331,3547,7847,5433,3394,4968,9983,3540,9224,6216,9665,8070,31,3555,4198,2626,9553,9724,4503,1951,9980,3975,6025,8928,2952,911,3674,6620,3745,6548,4985,5206,5777,1908,6029,2322,2626,2188,5639],
#     x=565610,
# ))      # 정답: 113
