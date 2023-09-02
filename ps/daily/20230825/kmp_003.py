#
# 교과서의 KMP 풀이
#    https://hwlang.de/algorithmen/pattern/kmpen.htm
#


from typing import List


def preprocess_kmp(pattern: str):
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

    while i < len_text:
        while j >= 0 and text[i] != pattern[j]:
            j = b[j]

        i += 1
        j += 1

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
text = "babbbbbabb"

# pattern = "Jump".lower()
# pattern = "BAABABAA"
# pattern = "cat"
# pattern = "leeto"
# pattern = "a"
# pattern = "issip"
# pattern = "BAABAB"
pattern = "bbab"


b = preprocess_kmp(pattern)
print(find_pattern(b, text, pattern))
