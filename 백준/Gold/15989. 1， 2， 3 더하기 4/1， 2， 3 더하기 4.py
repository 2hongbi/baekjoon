dp = [1] * 10001 # 1만 써서 합이 되는 경우는 모두가 갖고 있음 > dp 배열 초기화 시 1로 넣어놓음

# 2가 추가되는 경우 고려
for i in range(2, 10001):
    dp[i] += dp[i - 2]

# 3이 추가되는 경우 고려
for i in range(3, 10001):
    dp[i] += dp[i - 3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
