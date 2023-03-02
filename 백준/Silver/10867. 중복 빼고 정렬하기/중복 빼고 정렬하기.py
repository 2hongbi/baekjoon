import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr = list(set(arr))
arr.sort()

for i in range(len(arr)):
    print(arr[i], end=' ')