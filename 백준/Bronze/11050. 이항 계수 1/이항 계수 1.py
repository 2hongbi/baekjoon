n, k = map(int, input().split())
dp = [[0 for j in range(n + 1)] for i in range(n + 1)]

for i in range(0, n + 1):
    dp[i][1] = i # i에서 1개 선택하는 경우의 수
    dp[i][0] = 1 # i에서 1개도 선택하지 않는 경우의 수
    dp[i][i] = 1 # i에서 모두 선택하는 경우의 수

for i in range(2, n + 1):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] # 조합 기본 점화식

print(dp[n][k])