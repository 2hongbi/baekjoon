from collections import deque

def bfs(x, y, now_color):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and picture[nx][ny] == now_color and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


def bfs_color(x, y, now_color):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if now_color in 'RG' and picture[nx][ny] in 'RG':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif picture[nx][ny] == now_color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))



n = int(input())
picture = [list(input().strip()) for _ in range(n)]

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

visited = [[False] * n for _ in range(n)]
count1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, picture[i][j])
            count1 += 1

visited = [[False] * n for _ in range(n)]
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_color(i, j, picture[i][j])
            count2 += 1

print(count1, count2)