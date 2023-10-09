import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] *  (n + 1)

def dfs(v):
    visited[v] = True
    for curr_v in graph[v]:
        if not visited[curr_v]:
            dfs(curr_v)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)
print(count)