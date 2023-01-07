import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

remainder = [0] * M
remainder[0] = 1

total = 0
for i in range(N):
    total += A[i]
    remain = total % M
    remainder[remain] += 1

answer = 0
for i in range(M):
    if remainder[i] > 1:
        answer += (remainder[i] * (remainder[i] - 1) // 2)

print(answer)