import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

# 익은 토마토(1)를 시작점으로 탐색 시작하는 것이 중요
queue = deque()

# 토마토 상자에서 익은 토마토를 우선 큐에 넣기
for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 1:
            queue.append((i, j))


def bfs():
    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # 상자 내부에 있고, 토마토가 아직 익지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and tomato_box[nx][ny] == 0:
                queue.append((nx, ny))
                tomato_box[nx][ny] = tomato_box[x][y] + 1

bfs()

max_days = 0
all_rips = True

for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 0:
            all_rips = False
        max_days = max(max_days, tomato_box[i][j])

if all_rips:
    print(max_days - 1) # 첫 날이 1이니까 1 뺴기
else:
    print(-1)