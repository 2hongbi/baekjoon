import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 1-based index

for _ in range(m):
    a, b = map(int, input().split())
    # b를 해킹하면 a도 해킹할 수 있다는 지문 보기
    graph[b].append(a)

def bfs(v):
    visited = [False] * (n + 1)
    visited[v] = True
    queue = deque([v])
    count = 1 # 메모리 초과 해결 위해서

    while queue:
        curr_node = queue.popleft()

        for i in graph[curr_node]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = True

    return count


answer = []
max_val = 0
for i in range(1, n + 1):
    result = bfs(i)
    if max_val < result:
        max_val = result
        answer.clear()
        answer.append(i)
    elif max_val == result:
        answer.append(i)

print(*answer)