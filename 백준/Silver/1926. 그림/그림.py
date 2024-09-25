import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y):
    area = 1
    queue = deque([(x, y)])
    paper[x][y] = 0 # visited

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + cx, dy + cy

            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                area += 1
                paper[nx][ny] = 0
                queue.append((nx, ny))

    return area


count = 0 # 그림의 개수
max_area = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)
print(max_area)