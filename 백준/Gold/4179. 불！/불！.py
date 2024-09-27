import sys
from collections import deque

r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

fire_queue = deque()
jihun_queue = deque()

fire_time = [[-1] * c for _ in range(r)]
jihun_time = [[-1] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            jihun_queue.append((i, j))
            jihun_time[i][j] = 0
        if maze[i][j] == 'F':
            fire_queue.append((i, j))
            fire_time[i][j] = 0


def fire_bfs():
    while fire_queue:
        x, y = fire_queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if maze[nx][ny] != '#' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    fire_queue.append((nx, ny))


def jihun_bfs():
    while jihun_queue:
        x, y = jihun_queue.popleft()

        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
            print(jihun_time[x][y] + 1)
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if maze[nx][ny] == '.' and jihun_time[nx][ny] == -1:
                    if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                        jihun_time[nx][ny] = jihun_time[x][y] + 1
                        jihun_queue.append((nx, ny))

    else:
        print('IMPOSSIBLE')


fire_bfs()
jihun_bfs()