import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

def prefix_sum(arr):
    prefix = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + arr[i-1]

    return prefix

prefix = prefix_sum(numbers)


for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - (prefix[i - 1] if i > 0 else 0))