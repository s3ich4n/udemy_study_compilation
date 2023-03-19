def fibonacci_head(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    # 어떤 값은 동시에 계산되고, 스택 프레임도 쓴다 -> 어떤 면에서 비효율적
    # DP 로 일부 해결가능
    res1 = fibonacci_head(n - 1)
    res2 = fibonacci_head(n - 2)

    result = res1 + res2

    return result


print(fibonacci_head(5))
