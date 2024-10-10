import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(n)]

sushi_count = defaultdict(int) # 초밥 종류 카운트

sushi_count[c] = 1 # 쿠폰 초밥 미리 추가

for i in range(k):
    sushi_count[sushis[i]] += 1

max_count = len(sushi_count)

for i in range(1, n):
    prev_sushi = sushis[i - 1]
    sushi_count[prev_sushi] -= 1
    if sushi_count[prev_sushi] == 0:
        del sushi_count[prev_sushi]

    next_sushi = sushis[(i + k - 1) % n]
    sushi_count[next_sushi] += 1

    max_count = max(max_count, len(sushi_count))

print(max_count)