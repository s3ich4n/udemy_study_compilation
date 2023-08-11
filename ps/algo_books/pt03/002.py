class Quiz002:
    def length_of_longest_substr(self, s: str) -> int:
        used = {}         # 현재 문자를 키로 하는 해시 테이블!
        max_length = start = 0

        for index, char in enumerate(s):
            if char in used \
                and start <= used[char]:        # 슬라이딩 윈도우 밖에 있는 문자는 당장 비교할 수 없음
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length

if __name__ == "__main__":
    q = Quiz002()

    test1 = "abcabcbb"
    test2 = "bbbbb"
    test3 = "pwwkew"

    print(q.length_of_longest_substr(test1))
    print(q.length_of_longest_substr(test2))
    print(q.length_of_longest_substr(test3))
