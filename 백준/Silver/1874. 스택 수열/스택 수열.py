import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]

stack, ans = [], []
find = True
now = 1

for i in range(n):
    num = arr[i]

    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        find = False

if not find:
    print('NO')
else:
    print('\n'.join(ans))