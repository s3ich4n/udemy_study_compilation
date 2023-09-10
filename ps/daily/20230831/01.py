# https://school.programmers.co.kr/tryouts/85889/challenges

import collections


def solution(babbling):
    answer = 0

    # 이 값은 "동일하게" 존재해야함.
    #   진짜 단순하게... 문자열을 갖고와서 여기있는 문자열을 빼면?
    baby_babbling = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        position = collections.defaultdict(list)

        word_counter = 0

        for char in word:
            if not position[char]:
                break
            else:
                word_counter += 1

        if len(word) == word_counter:
            answer += 1

    return answer


print(solution(["yee", "u", "maa", "wyeoo"]))

# 2개 이상?
# 0: y, 1: e, 2: e
# ye 포함됨, 다 꺼내보니 yee임
# 

# 들어오는 값의 0, 1, 2 를 다 떼고, babbling의 0, 1, 2와 일일이 비교?
# yee
# 0:2는 있음 -> ye 추가
# 0:3은 없음 -> 제거

#
# yemawoo
# ye 포함됨, ma 포함됨, woo 포함됨
# 셋다 있나?

# aya
# ye
# woo
# ma
# 가 포함되어있으면? - 입력 문자열 '넷 중 하나라도 포함되어있으면' 정답
# 
# babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장
#     - 즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장함
