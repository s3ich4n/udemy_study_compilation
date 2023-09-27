#
# https://leetcode.com/problems/word-break/
#
# 어프로치 #1
#   이거 옹알이랑 비슷한 문제 아닌가?
#   regex로 첫 위치를 잡고 *로 마스킹하기?
#   한번 마스킹하면 동일한건 못찾을 것이기 때문에...
#
# 어프로치 #2
#   KMP를 구현해서 s에 대해 wordDict 문자열로 n번 순회하도록 함
#   찾았으면 wordDict 문자열에서 값을 "제거"
#   마지막에는 s가 전부 마스킹되었는지로 판별
#


import re

from typing import List


class Solution:
    @staticmethod
    def get_prefix(pattern: str) -> str:
        i = 0
        j = -1
        b = [-1 for _ in range(len(pattern) + 1)]

        while i < len(pattern):
            while j >= 0 and pattern[i] != pattern[j]:
                j = b[j]

            i += 1
            j += 1
            b[i] = j

        return b

    @staticmethod
    def find_pattern(b: List, text: str, pattern: str) -> (int, int):
        len_text = len(text)
        len_pat = len(pattern)
        result = []
        i = j = 0

        # 전체 문자열을 순회한다
        while i < len_text:

            # pattern과 다르면 점프한다
            while j >= 0 and text[i] != pattern[j]:
                j = b[j]

            i += 1
            j += 1

            # 이거까지만 비교하면, 패턴을 찾을 수 있다.
            if j == len_pat:
                result.append(i - j)
                j = b[j]

        if len(result) != 0:
            return result, len(pattern)

        else:
            return -1
        
    @staticmethod
    def mark_char(s: str, caught: int, point: int) -> str:
        """ 발견한 지점을 토대로 마스킹을 수행한다

        Args:
            s (str): 이상하다 판단되는 문자열
            caught (int): 탐지한 지점
            point (int): 문자열의 길이

        Returns:
            str: 마스킹된 문자열 결과
        """
        new_char = ""

        for starting_point in caught:
            for idx, char in enumerate(s):
                if starting_point <= idx < starting_point + point:
                    new_char += "*"
                else:
                    new_char += char

        return new_char

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ s 내에 있는 wordDict가 "겹치지 않고" 존재하는지 판별한다.

        Args:
            s (str): 문자열
            wordDict (List[str]): 겹치는지 확인하는 단어들

        Returns:
            bool: wordDict 내의 문자열이 겹치는지 아닌지 판별
        """
        for word in wordDict:
            prefix = self.get_prefix(word)
            caught, point = self.find_pattern(prefix, s, word)

            if caught == -1:
                return False

            else:
                # 0~4, 8~12가 한 루프 안에서 어떻게 처리되어야 할까?
                s = self.mark_char(s, caught, point)


s = Solution()
# s.wordBreak(s="leetcode", wordDict=["leet","code"])
s.wordBreak(s="applepenapple", wordDict=["apple","pen"])
s.wordBreak(s="catsandog", wordDict=["cats","dog","sand","and","cat"])
