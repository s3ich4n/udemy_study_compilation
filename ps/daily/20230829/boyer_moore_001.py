from collections import namedtuple
from typing import List, Union


FindStr = namedtuple("FindStr", ["found", "position"])


def findstr(text, pattern):
    i = len(pattern) - 1

    while i > 0:
        if text[i] != pattern[i]:
            return FindStr(False, i)
        i -= 1

    return FindStr(True, 0)


def bad_char():
    ...


def find_ptr_in_good_suffix_table(suffix_table: List[int], pattern: str):
    ...


def build_good_suffix_table(text: str, pattern: str) -> List[int]:
    """ 좋은 접미사 테이블을 생성한다.

    예를 들어 AABABA 의 경우...

    Args:
        text (str): _description_
        pattern (str): _description_

    Returns:
        List[int]: _description_
    """
    def _find_start_of_longest_border(pattern, border_check):
        starting_point = -1

        for right in range(len(pattern), 0, -1):
            if pattern[right:] == border_check:
                starting_point = len(pattern[right:])

        return starting_point

    good_suffix_table = [0 for _ in range(len(pattern) + 1)]

    pat_idx = len(pattern)

    for i in range(pat_idx, 0, -1):
        if i == len(pattern):
            good_suffix_table[i] = len(pattern) + 1
        else:
            good_suffix_table[i] = _find_start_of_longest_border(pattern, pattern[i:])

    return good_suffix_table


def search_pattern_from_text(text: str, pattern: str) -> Union[int, None]:
    """ Boyer-Moore 알고리즘대로 text에 pattern이 존재하는지 찾는다.

    Args:
        text (str): 패턴이 존재하는지 확인하려는 문자열
        pattern (str): 찾고자 하는 패턴
    """
    index = 0
    len_pattern = len(pattern)

    good_suffix = build_good_suffix_table(text, pattern)

    while index < len(text):
        # text를 뒤에서부터 pattern 길이만큼 순회하는게 목적
        result, internal_idx = findstr(text[index:len_pattern], pattern)
        if not result:
            ptr = bad_char(internal_idx)
            if ptr < 0:
                ptr = find_ptr_in_good_suffix_table(good_suffix, pattern)

            index += 1
        
        else:
            return text[index:len_pattern]

    return result[1]


# text = "babbbabbab bab babbabab"
text = "babbabab"
pattern = "aababa"


print(search_pattern_from_text(text, pattern))
