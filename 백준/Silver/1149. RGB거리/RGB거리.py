import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)] # r, g, b

dp = [[0] * 3 for _ in range(n)]

# initialize
dp[0][0] = cost[0][0] # red
dp[0][1] = cost[0][1] # green
dp[0][2] = cost[0][2] # blue

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0] # i번 집을 빨강으로 칠하기
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1] # i번 집을 초록으로 칠하기
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2] # i번 집을 파랑으로 칠하기


print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))