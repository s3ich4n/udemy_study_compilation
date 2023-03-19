def solution(a, b):
    if b == 1:
        return a

    if b % 2 != 0:
        return a + solution(a << 1, b >> 1)

    if b % 2 == 0:
        return solution(a << 1, b >> 1)


print(solution(23, 78))
