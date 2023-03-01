from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deque = deque()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        deque.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deque.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(deque.popleft()) if deque else print(-1)
    elif cmd[0] == 'pop_back':
        print(deque.pop()) if deque else print(-1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        print(0) if deque else print(1)
    elif cmd[0] == 'front':
        print(deque[0]) if deque else print(-1)
    elif cmd[0] == 'back':
        print(deque[-1]) if deque else print(-1)