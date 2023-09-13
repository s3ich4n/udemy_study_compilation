

# 이건 그리디 접근이다. DP로 풀어야한다.
# 반례
#   642를 넣으면 11이 나온다. 원래는 10이어야 함
#   642//3을 하면 11번 타지만,
#   642//2를 하면 10번 타고 끝나기 때문이다.
# https://www.acmicpc.net/board/view/114529
# https://www.acmicpc.net/board/view/120706


# n = int(input())
# def make_one(n):
#     def judge(number: int):
#         if number % 3 == 0:
#             return number // 3
#         elif number % 2 == 0:
#             return number // 2
#         else:
#             return number - 1

#     counter = 1
#     curr = judge(n)

#     while True:
#         print(f"debug... {curr} [{counter}th]")
#         if curr == 1:
#             break
#         else:
#             curr = judge(curr)
#             counter += 1

#     print(counter)


# make_one(n)

# import timeit
# print(f"{timeit.timeit('make_one(n)', number=1, globals=globals()):.f}")

# 최소한의 방법으로 타야한다.
# 그러면, dp로 각 결과를 잘 저장하고 있다가, 가장 짧게 결과가 나오는 쪽을 리턴하면 된다.

n = int(input())
dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
