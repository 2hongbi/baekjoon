# https://www.acmicpc.net/problem/11060

n = int(input())
a = list(map(int, input().split()))

# 최소 점프를 저장하기 위해 큰 수로 초기값 지정 : 어차피 점프 횟수가 n + 1 이상이면 실패임
dp = [n + 1] * n
dp[0] = 0

# 각 칸에 대해 그 칸에서 점프할 수 있는 최대 범위까지의 점프 값을 현재 칸의 점프값 + 1 과 비교 -> 최소값 갱신
for i in range(n):
    for j in range(1, a[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i] + 1, dp[i + j])


if dp[n - 1] == n + 1:
    print(-1)
else:
    print(dp[n - 1])