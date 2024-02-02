from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
for i in range(n + 1):
    graph[i].sort()


visited = [False] * (n + 1)
def dfs(node):
    print(node, end=' ')
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            visited[next_node] = True
dfs(v)

print()

visited = [False] * (n + 1)
def bfs(node):
    queue = deque([node])
    visited[node] = True

    while queue:
        curr_node = queue.popleft()
        print(curr_node, end=' ')
        visited[curr_node] = True

        for next_node in graph[curr_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

bfs(v)