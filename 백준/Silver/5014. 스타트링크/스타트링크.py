from collections import deque

f, s, g, u, d = map(int, input().split())


def bfs(start):
    visited = [False] * (f + 1)
    queue = deque([(start, 0)])  # 현재 층, 버튼 누른 횟수
    visited[start] = True

    while queue:
        curr, cnt = queue.popleft()

        if curr == g:
            return cnt

        if curr + u <= f and not visited[curr + u]:
            visited[curr + u] = True
            queue.append((curr + u, cnt + 1))

        if curr - d >= 1 and not visited[curr - d]:
            visited[curr - d] = True
            queue.append((curr - d, cnt + 1))

    return "use the stairs"


print(bfs(s))