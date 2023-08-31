#
# problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#


from typing import Union


# haystack = "A Quick Brown Fox Jumps Over The Lazy Dog.".lower()
# haystack = "BABAA ABABA BAABABAA BAB"
# haystack = "ttacatcad"
# haystack = "leetcode"
# haystack = "aaa"
# haystack = "mississippi"
# haystack = "BAABAABAB"
haystack = "babbbbbabb"

# needle = "Jump".lower()
# needle = "BAABABAA"
# needle = "cat"
# needle = "leeto"
# needle = "a"
# needle = "issip"
# needle = "BAABAB"
needle = "bbab"


def get_border(needle: str):
    def _get_border_inside(_s: str):
        count = 0

        if len(_s) != 0:
            left, right = 0, len(_s)

            for _ in range(len(_s)):
                if _s[:left] == _s[right:]:
                    count = len(_s[:left])
                left += 1
                right -= 1

            return count

        else:
            return -1

    result = []

    for idx, _ in enumerate(range(len(needle) + 1)):
        result.append(_get_border_inside(needle[:idx]))

    return result


def get_pattern_from_str(haystack, needle) -> Union[str, None]:
    """ 문자열로부터 패턴을 구해온다

    Args:
        haystack (_type_): _description_
        needle (_type_): _description_
    """
    idx, left, right = 0, 1, 1
    while idx < len(haystack):
        # 패턴과 문자열이 같다면?
        # 더 찾아본다
        if needle[:left] == haystack[idx:idx + right]:
            if haystack[idx:idx + right] == needle:
                return idx

            left += 1
            right += 1

        # 불일치가 일어나면?
        # 경계만큼 움직인다
        else:
            idx += (len(haystack[idx:idx + right - 1]) - border[right - 1])
            right = 1
            left = 1

    return -1


border = get_border(needle)
print(get_pattern_from_str(haystack, needle))
