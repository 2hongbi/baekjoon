n = int(input())

# 0부터 n까지 모든 수를 소수로 초기화
primes = [True] * (n + 1)
primes[0] = primes[1] = False # 0과 1은 소수가 아님

for i in range(2, int(n**0.5)+1):
    if primes[i]:
        for j in range(i*i, n+1, i):
            primes[j] = False

# 소수 여부를 숫자로 초기화
primes = [i for i, prime in enumerate(primes) if prime]

count = 0
start, end = 0, 0
current_sum = 0

while end <= len(primes):
    if current_sum == n:
        count += 1
        # 현재 합이 n과 같으면 경우의 수 증가시키고, start 이동
        current_sum -= primes[start]
        start += 1
    elif current_sum < n: # 현재 합이 n보다 크면 끝 포인터 증가
        if end < len(primes):
            current_sum += primes[end]
        end += 1
    else: # 현재 합이 n보다 작으면 시작 포인터 증가
        current_sum -= primes[start]
        start += 1


print(count)