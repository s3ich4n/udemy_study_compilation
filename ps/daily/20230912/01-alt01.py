#
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
#

import cProfile
import timeit
import pathlib

import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        answer = 0
        # 이렇게 하면 일일이 count를 세니까 느려진다! cProfile로 이걸 잡을 수 있었다.
        # s_count = {i: s.count(i) for i in s}

        s_count = collections.defaultdict(int)

        for i in s:
            s_count[i] += 1

        s_count = list(s_count.values())
        len_s_count = len(s_count)

        prev = 0
        while prev <= len_s_count + 1:
            curr = -1
            for idx in range(prev + 1, len_s_count):
                if s_count[prev] != 0 and s_count[prev] == s_count[idx]:
                    curr = idx

            if curr != -1:
                answer += 1
                s_count[prev] -= 1
                prev = 0

            else:
                prev += 1

        return answer


s = Solution()
# print(s.minDeletions("aab"))
# print(s.minDeletions("aaabbbcc"))
# print(s.minDeletions("ceabaacb"))
# print(s.minDeletions("abcabc"))
# print(s.minDeletions("bbcebab"))        # 2 가 나와야함

with open(pathlib.Path().cwd() / "testcase60", "r") as f:
    print(
        s.minDeletions(f.readline())
    )

    # 1. timeit으로 수행시간 테스트. 아래와 같이 실행함:
    # execution_time = timeit.timeit(
    #     "s.minDeletions(f.readline())",
    #     globals=globals(),
    #     number=1,
    # )
    # print(f"quicksort() execution time: {execution_time}")

    # 2. cProfile로 어떤 구문이 얼마만큼 실행되었는지 프로파일링
    #    stdout으로 실행내용이 나옴. 아래와 같이 실행함:
    # cProfile.run("s.minDeletions(f.readline())")
