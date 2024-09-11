import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()  # 정점 번호가 작은 것부터 방문하기 위해서

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
        current = queue.popleft()
        print(current, end=' ')

        for g in graph[current]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True


visited = [False] * (n + 1)
dfs(v, visited)
print()
bfs(v)