import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(input().strip())

arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))

print('\n'.join(arr))