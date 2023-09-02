import collections
from typing import List, Dict


def build_bad_char_table(pattern: str) -> Dict[str, int]:
    """ bad char 점프 테이블을 작성

    t 꺼냄
    t = 0
    e = 1
    x = 2
    t 또나왔으니 t = 3

    -> 이걸 defaultdict에

    Args:
        pattern (str): _description_

    Returns:
        Dict[str, int]: _description_
    """
    tbl = collections.defaultdict(int)

    for idx, val in enumerate(pattern):
        tbl[val] = idx if val in pattern else -1

    return tbl


def build_good_suffix_table_pt01(pattern: str, f: List, s: List):
    """ Good suffix 테이블 작성 pt 1 을 진행한다

    case 1) 패턴 내 어딘가에 일치하는 접미사가 있는 경우
    case 2) 일치하는 패턴의 "일부"가 패턴 처음에 나타나는 경우

    단 동일 패턴으로 "확장"하면 안됨.
        pat = "AABABA" 에서, pat[4]의 값은 확장시 pat[2] 값과 같기 때문.

    Args:
        pattern (str): 패턴
        f (List): 해당 접미부에서 가장 넓은 경계가 시작되는 패턴 내의 위치
        s (List): 이동 거리
    """
    i = len(pattern)
    j = i + 1
    f[i] = j    # 맨 끝값은 경계값이 없으므로 len(pattern) + 1값

    while i > 0:
        while j <= len(pattern) and pattern[i-1] != pattern[j-1]:
            # 역으로 쫓아갈 수 있으면?
            if s[j] == 0:
                s[j] = j - i
            j = f[j]

        i -= 1
        j -= 1
        f[i] = j


def build_good_suffix_table_pt02(pattern: str, f: List, s: List):
    """
    """
    j = f[0]

    for idx in range(len(pattern)):
        if s[idx] == 0:
            s[idx] = j
        if idx == j:
            j = f[j]


def find_pattern(text: str, pattern: str) -> int:
    """ text 내에 패턴이 있는지 찾는다

    Args:
        text (str): 패턴을 찾으려는 문자열
        pattern (str): 패턴

    Returns:
        int: 패턴이 처음 등장한 위치
    """
    i = 0
    result = []

    # 이 조건만 이해하면 될듯?
    while i <= (len(text) - len(pattern)):
        cur = len(pattern) - 1

        while cur >= 0 and pattern[cur] == text[i + cur]:
            cur -= 1

        if cur < 0:
            result.append(i)
            i += s[0]

        else:
            i += max(cur - bad_char[text[i + cur]], s[cur + 1])

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
pattern = "bbabc"


bad_char = build_bad_char_table(pattern)
f = [0 for _ in range(len(pattern) + 1)] #  항목 f [i]에는 위치 i 에서 시작하는 패턴 접미사의 가장 넓은 경계의 시작 위치가 포함
s = [0 for _ in range(len(pattern) + 1)] #  이동위치
build_good_suffix_table_pt01(pattern, f, s)
build_good_suffix_table_pt02(pattern, f, s)
print(find_pattern(text, pattern))

a = 1
