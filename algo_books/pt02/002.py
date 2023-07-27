class Quiz002:
    def longest_palindroms(self, s: str) -> str:
        def expand(self, left: int, right: int):
            # 중간값을 기점으로 좌우로 비교해줌
            while left > 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]        # left+1 : right 임에 유의!

        # 뒤집어도 똑같거나, 길이가 2 이하면 의미가없음
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            # 셋 중 제일 긴 놈(key=len)이 result로.
            result = max(
                result,
                expand(self, i, i+1),       # 투 포인터 1
                expand(self, i, i+2),       # 투 포인터 2
                key=len,
            )

        return result


if __name__ == "__main__":
    quiz1 = "babad"
    quiz2 = "cbbd"

    quiz3 = "971232323232134351"

    q = Quiz002()

    print(q.longest_palindroms(quiz1))
    print(q.longest_palindroms(quiz2))
    print(q.longest_palindroms(quiz3))
