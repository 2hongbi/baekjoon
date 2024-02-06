n = int(input())

def fibonacci(n):
    dp = [0] * (n+1)  # DP 테이블 초기화
    dp[1] = 1  # 초기 조건 설정
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]  # 점화식에 따라 F(n) 계산
    return dp[n]

print(fibonacci(n))