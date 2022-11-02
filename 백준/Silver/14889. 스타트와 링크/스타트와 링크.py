import sys

input = sys.stdin.readline

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
min_diff = int(1e9) # 가능한 최댓값이 10억 미만이라면 무한(INF)의 값으로 1e9를 이용할 수 있음(1 * 10^9), 2e9는 무한대 값 표시


def dfs(depth, idx):
    global min_diff
    if depth == N // 2:
        power1, power2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:   # 방문처리 -> 스타스팀
                    power1 += people[i][j]
                elif not visited[i] and not visited[j]: # 방문처리 X -> 링크팀
                    power2 += people[i][j]
        min_diff = min(min_diff, abs(power1 - power2))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


dfs(0, 0)
print(min_diff)

