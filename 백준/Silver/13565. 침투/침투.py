from collections import deque


def bfs(starts, grid, m, n):
    queue = deque(starts)

    # 1. 탐색 시작 노드를 큐에서 꺼내 방문처리
    visited = [[False] * n for _ in range(m)]
    for x, y in starts:
        visited[x][y] = True

    # 2. 큐에서 노드를 꺼내 해당 인접 노드 중 방문하지 않은 노드를 큐에 삽입
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        x, y = queue.popleft()

        if x == m - 1: # 마지막 행 도달
            return "YES"

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '0':
                visited[nx][ny] = True
                queue.append((nx, ny))

    return "NO"


m, n = map(int, input().split())
grid = [input().strip() for _ in range(m)]

# 첫 행에서 시작할 수 있는 지점들 찾기 : 0이면 전류 통함, 1이면 전류 통하지 않음
starts = [(0, j) for j in range(n) if grid[0][j] == '0']

# bfs 실행
print(bfs(starts, grid, m, n))