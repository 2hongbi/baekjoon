import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 누적합 계산
def prefix_sum(arr):
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix

prefix = prefix_sum(numbers)

# 나머지 개수 저장할 딕셔너리
mod_count = [0] * m
mod_count[0] = 1

count = 0

for p in prefix:
    remainder = p % m
    count += mod_count[remainder]
    mod_count[remainder] += 1

print(count)