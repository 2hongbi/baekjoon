# https://www.acmicpc.net/problem/2156
# 1. i번째 포도주를 마시지 않는 경우
# 2. i번째 포도주를 마시고, i - 1번째 포도주도 마시는 경우
# 3. i번째 포도주 잔만 마시는 경우:


n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 1)

if n > 0:
    dp[1] = wine[1]

if n > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2])

print(dp[n])