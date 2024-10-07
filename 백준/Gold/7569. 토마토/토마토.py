import sys
from collections import deque
input = sys.stdin.readline

dxs, dys, dzs = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
tomato = []
queue = deque()

for z in range(h): # z > y > x 순으로 저장하기
    layer = []
    for y in range(n):
        row = list(map(int, input().split()))
        layer.append(row)
        for x in range(m):
            if row[x] == 1:
                queue.append((x, y, z))
    tomato.append(layer)

def bfs():
    while queue:
        x, y, z = queue.popleft()

        for dx, dy, dz in zip(dxs, dys, dzs):
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                queue.append((nx, ny, nz))

bfs()

max_days = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato[z][y][x] == 0:
                print(-1)
                exit(0)
            max_days = max(max_days, tomato[z][y][x])

print(max_days - 1)