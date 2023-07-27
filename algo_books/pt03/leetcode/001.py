# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from collections import OrderedDict
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def runner(nums: List[int], index: int, result: int):
            while True:
                if nums[index] != nums[index + 1]:
                    if nums[index + 1] != nums[index + 2]:
                        answer.append(nums[index])
                        return (result + 2, index + 2)
                    else:
                        answer.append(nums[index])
                        return (result + 1, index + 1)
                elif nums[index] != nums[index + 2]:
                    answer.append(nums[index])
                    return (result + 1, index + 2)
                else:
                    index += 1

        answer = []
        result = 0
        index = 0
        max_index = len(nums) - 1

        try:
            while True:
                result, index = runner(nums, index, result)
        except Exception:
            if index + 1 == max_index:
                answer.append(nums[index])
                result += 2
            elif index + 2 == max_index:
                answer.append(nums[index])
                result += 1
            else:
                answer.append(nums[index])
                result += 1

        return answer


if __name__ == "__main__":
    q = Solution()

    test999 = [1, 1, 3, 3, 0, 1, 1]
    test12 = [4, 4, 4, 3, 3]
    # test1 = [1, 1, 2]
    # test2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # test3 = [1, 2]
    # test4 = [1, 1, 2, 3]

    # print(q.removeDuplicates(test1))
    # print(q.removeDuplicates(test2))
    # print(q.removeDuplicates(test3))
    print(q.removeDuplicates(test999))
    print(q.removeDuplicates(test12))
