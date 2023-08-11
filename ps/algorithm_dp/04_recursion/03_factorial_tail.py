def factorial_tail(
    n: int,
    accumulator: int = 1,
):
    if n == 0:
        return accumulator

    factorial_tail(n - 1, n * accumulator)


print(factorial_tail(5))
