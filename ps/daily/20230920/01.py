#
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
#
# 어프로치 #1
#   그냥 로직 가는대로...
#   좀만 복잡해지니까 어디서 어떻게 되는지 감이 안 온다...!
#
#   투포인터는 "정렬된" 값에서 사용할 수 있다 << 이걸 기억했어야했음
#
# 어프로치 #1 - revisited
#   투포인터를 사용하되, 슬라이딩 윈도우 형식으로 접근한다.
#
#   다만, 구해야 할 사항은 len(subarray) == sum(nums) - x 인 subarray를 구하는 것이다
#   저 subarray의 가장 긴 길이 Y를 구하고, sliding window를 축소(shrinkable window임)하여 다시 찾아간다.
#   이 슬라이딩 윈도우를 천천히 조이면서 답 찾는게 눈에 보여야된다...
#
#   이런 발상의 전환이 내가 가장 안 되는 부분이고, 몇 번이고 연습해야한다!
#


from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x

        if target == 0:
            return len(nums)

        max_len = cur_sum = left = 0

        for right, val in enumerate(nums):
            cur_sum += val
            # 이 루프는 subarray 조건이 충족되는 그 때 돈다
            while left <= right and cur_sum > target:
                # subarray의 크기를 줄여서 다시 찾아본다
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                # 인덱스 right - left 이므로 + 1을 해야 길이비교가 된다
                max_len = max(max_len, right - left + 1)

        # max_len이 0이면 subarray를 못찾았다는 뜻이므로 -1
        return len(nums) - max_len if max_len else -1


s = Solution()
# print(s.minOperations(nums=[1,1,4,2,3], x=5))          # 정답: 2
print(s.minOperations(nums=[5,6,7,8,9], x=4))          # 정답: -1
print(s.minOperations(nums=[3,2,20,1,1,3], x=10))      # 정답: 5
# print(s.minOperations(nums=[1,1], x=3))      # 정답: 5
# print(s.minOperations(nums=[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], x=134365))      # 정답: 16
# print(s.minOperations(
#     nums=[5207,5594,477,6938,8010,7606,2356,6349,3970,751,5997,6114,9903,3859,6900,7722,2378,1996,8902,228,4461,90,7321,7893,4879,9987,1146,8177,1073,7254,5088,402,4266,6443,3084,1403,5357,2565,3470,3639,9468,8932,3119,5839,8008,2712,2735,825,4236,3703,2711,530,9630,1521,2174,5027,4833,3483,445,8300,3194,8784,279,3097,1491,9864,4992,6164,2043,5364,9192,9649,9944,7230,7224,585,3722,5628,4833,8379,3967,5649,2554,5828,4331,3547,7847,5433,3394,4968,9983,3540,9224,6216,9665,8070,31,3555,4198,2626,9553,9724,4503,1951,9980,3975,6025,8928,2952,911,3674,6620,3745,6548,4985,5206,5777,1908,6029,2322,2626,2188,5639],
#     x=565610,
# ))      # 정답: 113
