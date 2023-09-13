n = int(input())
dp = [0 for _ in range(n + 1)]

def fib(n: int):
    dp[0] = 0
    dp[1] = 1
    
    for x in range(2, n + 1):
        dp[x] = dp[x - 1] + dp[x - 2]
    
    print(dp[n])

fib(n)
