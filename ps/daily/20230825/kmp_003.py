#
# 교과서의 KMP 풀이
#    https://hwlang.de/algorithmen/pattern/kmpen.htm
#


from typing import List


def preprocess_kmp(pattern: str) -> List[int]:
    """ 상기 정리, 증명, 정의를 활용하여, KMP에 사용할 문자열을 생성한다.

    Args:
        pattern (str): 문자열 패턴

    Returns:
        List[int]: KMP 탐색에 사용할 패턴의 스킵값
    """
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


def find_pattern(b: List, text: str, pattern: str) -> int:
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
        return result

    else:
        return -1


# text = "A Quick Brown Fox Jumps Over The Lazy Dog.".lower()
# text = "BABAA ABABA BAABABAA BAB"
# text = "ttacatcad"
# text = "leetcode"
# text = "aaa"
# text = "mississippi"
# text = "BAABAABAB"
# text = "babbbbbabb"
text = "bbabbb aaabababaa"

# pattern = "Jump".lower()
# pattern = "BAABABAA"
# pattern = "cat"
# pattern = "leeto"
# pattern = "a"
# pattern = "issip"
# pattern = "BAABAB"
pattern = "ababaa"


b = preprocess_kmp(pattern)
print(find_pattern(b, text, pattern))
