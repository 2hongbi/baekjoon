import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

count_list = []

dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            count_list.append(bfs(i, j))

count_list.sort()
print(len(count_list))
print(*count_list, sep='\n')