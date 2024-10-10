import sys
from collections import deque
input = sys.stdin.readline

def bfs(v, graph, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        g = queue.popleft()
        next_node = graph[g]
        if not visited[next_node]:
            queue.append(next_node)
            visited[next_node] = True


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    graph = [0] + arr
    visited = [False] * (n + 1)

    cycle_count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i, graph, visited)
            cycle_count += 1

    print(cycle_count)