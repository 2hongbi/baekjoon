# https://www.acmicpc.net/problem/7562
from collections import deque

# 나이트의 8가지 이동 방향
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs(l, start, end):
    visited = [[False] * l for _ in range(l)]
    queue = deque([(start[0], start[1], 0)])  # 현재 위치의 x, y, 이동 횟수

    while queue:
        x, y, depth = queue.popleft()
        if (x, y) == (end[0], end[1]):
            return depth

        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, depth + 1))

    return -1 # 도달할 수 없는 경우


test_cases = int(input())
for _ in range(test_cases):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(bfs(l, start, end))