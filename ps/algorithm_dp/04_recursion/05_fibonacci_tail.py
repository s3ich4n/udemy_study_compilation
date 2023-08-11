def fibonacci_tail(
    n: int,
    fib1: int = 0,
    fib2: int = 1,
):
    if n == 0:
        return fib1

    if n == 1:
        return fib2

    # 계속 계산해서 마지막으로 계산된 fib1, fib2가 출력되도록 함
    # fib1 값은 fib2로 처리
    # fib2 값은 fib1 + fib2 값으로 처리
    # 한번 덜 도는 부분도 주의
    return fibonacci_tail(n - 1, fib2, fib1 + fib2)

print(fibonacci_tail(10))
