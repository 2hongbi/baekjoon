import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')

    for g in graph[v]:
        if not visited[g]:
            dfs(g, visited)


def bfs(v):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True

    while queue:
        g = queue.popleft()
        print(g, end=' ')
        for g in graph[g]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)


visited = [False] * (n + 1)
dfs(v, visited)
print()
bfs(v)