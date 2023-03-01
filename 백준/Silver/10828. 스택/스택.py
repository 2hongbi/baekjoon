import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        print(0) if stack else print(1)
    elif order[0] == 'top':
        print(stack[-1]) if stack else print(-1)