n = int(input())

# 메모이제이션을 위한 리스트 초기화
memo = [0] * (n + 1)

def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if memo[x] != 0: # 이미 계산한 값이면 메모 반환
        return memo[x]
    memo[x] = fibo(x - 1) + fibo(x - 2)
    return memo[x]


print(fibo(n))