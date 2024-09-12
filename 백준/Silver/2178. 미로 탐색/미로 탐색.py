from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input()))
    for _ in range(n)
]

visited = [[False] * m for _ in range(n)]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                grid[nx][ny] = grid[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True


bfs(0, 0)
print(grid[n - 1][m - 1])