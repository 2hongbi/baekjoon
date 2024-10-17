import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1


visited = [[False] * n for _ in range(m)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    count = 1
    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count


answer = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            answer.append(bfs(i, j))

print(len(answer))
print(*sorted(answer))