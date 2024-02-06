n, m = map(int, input().split()) # 가로, 세로
battlefield = [input() for _ in range(m)]
visited = [[False] * n for _ in range(m)]

def dfs(x, y, team):
    if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or battlefield[x][y] != team:
        return 0

    visited[x][y] = True
    size = 1

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        size += dfs(x + dx, y + dy, team)

    return size


power_w, power_b = 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if battlefield[i][j] == 'W':
                power_w += dfs(i, j, 'W') ** 2
            elif battlefield[i][j] == 'B':
                power_b += dfs(i, j, 'B') ** 2

print(power_w, power_b)