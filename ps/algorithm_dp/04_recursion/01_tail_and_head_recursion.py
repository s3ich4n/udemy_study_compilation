def tail(n):
    print(f"calling tail: n={n}")

    # 탈출 조건
    if n == 0:
        return

    # 작동
    print(n)

    # 재귀호출
    tail(n-1)


def head(n):
    print(f"calling head: n={n}")

    # 탈출 조건
    if n == 0:
        return

    # 재귀호출
    head(n-1)

    # 작동
    print(n)


tail(5)
head(5)
