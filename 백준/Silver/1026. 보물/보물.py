import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

s = 0
for aa, bb in zip(a, b):
    s += aa * bb

print(s)