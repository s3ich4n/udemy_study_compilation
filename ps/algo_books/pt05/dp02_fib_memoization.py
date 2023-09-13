
def solution(n):
    def fib(n):
        if n <= 1:
            return n

        if dp[n]:
            return dp[n]
        dp[n] = fib(n - 1) + fib(n - 2)

        return dp[n]

    dp = [0 for _ in range(n + 1)]

    return fib(n)


print(solution(10))
