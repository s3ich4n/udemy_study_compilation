# https://school.programmers.co.kr/tryouts/85889/challenges

import re


def solution(babbling):
    answer = 0
    baby_babbling = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        for baby_word in baby_babbling:
            if baby_word in word:
                word = word.replace(baby_word, '*' * len(baby_word))
        if word.count('*') == len(word):
            answer += 1

    return answer


# print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["wyeoo", "yemawoo"]))

# wyeoo는...
# ye를 지우면 원본문자열.find()의 결과가 0이 아니다.

# yemawoo는...
# ye