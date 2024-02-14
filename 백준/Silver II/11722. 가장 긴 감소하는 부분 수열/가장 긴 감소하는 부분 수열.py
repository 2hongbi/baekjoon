n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n # 각 수열의 초기값은 1이기 떄문

for i in range(1, n):
    for j in range(0, i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))