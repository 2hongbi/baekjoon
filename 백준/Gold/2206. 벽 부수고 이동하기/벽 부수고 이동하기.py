from collections import deque

dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

def bfs(n, m, graph):
    # 3차원 visited -> visited[x][y][0] : 벽을 안 부순 상태, visited[x][y][1] : 벽을 부순 상태
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, is_broken = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][is_broken]

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][is_broken] == 0:
                    visited[nx][ny][is_broken] = visited[x][y][is_broken] + 1
                    queue.append((nx, ny, is_broken))

                # 벽이지만, 벽을 부수지 않은 상태에서 부술 수 있는 경우
                if graph[nx][ny] == 1 and is_broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][is_broken] + 1
                    queue.append((nx, ny, 1))

    return -1

print(bfs(n, m, graph))