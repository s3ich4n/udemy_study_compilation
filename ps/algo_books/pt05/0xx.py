from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majority_element(nums[:half])
        b = self.majority_element(nums[half:])

        # 좌/우를 가리는걸 이런식으로 한다!
        # [b, a]는 걍 리스트고
        # [nums.count(a) > half] 값은 True, False를 리턴한다.
        return [b, a][nums.count(a) > half]


if __name__ == "__main__":
    q = Solution()

    test1 = [3, 2, 3]
    test2 = [2, 2, 1, 1, 1, 2, 2]
    test3 = [1, 2, 1, 3, 1, 4, 1, 1]

    print(q.majority_element(test1))
    print(q.majority_element(test2))
    print(q.majority_element(test3))
