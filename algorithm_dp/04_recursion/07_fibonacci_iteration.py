def solution(
    n: int,
) -> int:
    fib1 = 0
    fib2 = 1

    for _ in range(0, n - 1):
        fib2, fib1 = fib1 + fib2, fib2

    return fib2


print(solution(2))