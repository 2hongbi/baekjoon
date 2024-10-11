import sys
input = sys.stdin.readline

n = int(input())
numbers = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    if t in numbers:
        print(1)
    else:
        print(0)