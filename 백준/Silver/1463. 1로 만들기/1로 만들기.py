import sys
input = sys.stdin.readline

count = 0
X = int(input())

dp = [0] * (X + 1)  # i에서 1로 만드는 데 걸리는 최소 연간 개수
for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1  # 1을 빼는 연산 먼저 -> 1 연산을 한 셈으로 개수 카운트
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:  # 처음에는 if ~ elif 로 했는데 한꺼번에 2, 3 나누기 처리를 해도 되는 것
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[X])