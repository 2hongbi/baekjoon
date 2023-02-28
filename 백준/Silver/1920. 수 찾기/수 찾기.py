import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

for a in arr:
    if a in A:
        print('1')
    else:
        print('0')