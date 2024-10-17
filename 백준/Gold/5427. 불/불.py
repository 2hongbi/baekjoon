import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        if visited[x][y] != 'FIRE':
            flag = visited[x][y]
        else:
            flag = 'FIRE'

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < h and 0 <= ny < w:
                if maps[nx][ny] == '.' and visited[nx][ny] == 0:
                    if flag == 'FIRE':
                        visited[nx][ny] = 'FIRE'
                    else:
                        visited[nx][ny] = flag + 1
                    queue.append((nx, ny))
            else:
                if flag != "FIRE":
                    return flag

    return "IMPOSSIBLE"


for _ in range(t):
    w, h = map(int, input().split())
    maps = [list(input().strip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    queue = deque()

    for i in range(h):
        for j in range(w):
            if maps[i][j] == '@':
                start = (i, j)
                maps[i][j] = '.'
                visited[i][j] = 1
            elif maps[i][j] == '*':
                visited[i][j] = 'FIRE'
                queue.append((i, j))

    queue.append(start)
    print(bfs())