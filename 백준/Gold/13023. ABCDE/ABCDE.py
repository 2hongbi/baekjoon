import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())

friends = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    friends[u].append(v)
    friends[v].append(u)


visited = [False] * n

def dfs(v, depth):
    if depth == 5:
        print(1)
        sys.exit() # 프로그램 종료

    # 현재 노드 방문처리
    visited[v] = True

    for g in friends[v]:
        if not visited[g]:
            dfs(g, depth + 1)

    visited[v] = False


# 모든 노드 탐색
for i in range(n):
    dfs(i, 1)

print(0)


