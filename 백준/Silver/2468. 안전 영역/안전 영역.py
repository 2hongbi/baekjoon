import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
def bfs(x, y, height, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))



max_safe_areas = 0
max_height = max(max(row) for row in graph)

for height in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    safe_area_count = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and not visited[i][j]:
                bfs(i, j, height, visited)
                safe_area_count += 1

    max_safe_areas = max(safe_area_count, max_safe_areas)

print(max_safe_areas)