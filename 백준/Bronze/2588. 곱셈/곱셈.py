import sys
input = sys.stdin.readline

a = int(input())
b = list(map(str, input().strip()))

for i in range(2, -1, -1):
    print(a * int(b[i]))
print(a * int(''.join(b)))