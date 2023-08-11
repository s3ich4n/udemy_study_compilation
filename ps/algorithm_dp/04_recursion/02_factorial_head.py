def factorial_head(n):

    if n == 0:
        return 1

    result1 = factorial_head(n-1)

    result2 = n * result1

    return result2

print(factorial_head(10))

