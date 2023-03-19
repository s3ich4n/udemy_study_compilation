def solution(a, b):
    result = 0

    while b > 0:
        # b값이 홀수가 되면?
        if b ^ 1 == b - 1:
            result = result + a

        a <<= 1
        b >>= 1

    return result


solution(23, 78)
