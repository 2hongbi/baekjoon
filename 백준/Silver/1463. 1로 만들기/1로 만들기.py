X = int(input())
dp = [0] * (X + 1)  # dp = 각 인덱스의 숫자가 1이 되는데 필요한 연산의 최솟값

for i in range(2, X+1):
    dp[i] = dp[i - 1] + 1   # 1을 뺴는 연산 1회 진행
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[X])