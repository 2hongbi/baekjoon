import sys
from collections import deque
input = sys.stdin.readline


# 도시 개수 n, 도로 개수 m, 거리 정보 k, 출발 도시 x
# 모든 도로의 거리는 1
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
answer = []


for _ in range(m):
    # 단방향 도로
    s, e = map(int, input().split())
    graph[s].append(e)


def bfs(v):
    queue = deque([v])
    visited[v] += 1

    while queue:
        curr_city = queue.popleft()

        for next_city in graph[curr_city]:
            if visited[next_city] == -1: # == not visited
                queue.append(next_city)
                visited[next_city] = visited[curr_city] + 1

bfs(x)

for i in range(n + 1):
    if visited[i] == k:
        answer.append(i)


if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)