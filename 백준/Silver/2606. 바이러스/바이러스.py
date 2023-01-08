import sys

input = sys.stdin.readline

n = int(input())    # 컴퓨터 개수
nodes = int(input())    # 연결선 개수
graph = [[] for _ in range(n + 1)]  # 그래프 초기화

for _ in range(nodes):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


visited = [False] * (n + 1)
dfs(1)
print(sum(visited) - 1)