from collections import deque

# 상, 하, 좌, 우로 이동할 수 있는 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS로 연결된 배추 군집을 탐색
def bfs(x, y, farm, visited, N, M):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        curr_x, curr_y = queue.popleft()

        # 상하좌우로 인접한 배추를 확인
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            # 범위 안에 있고, 배추가 있으며, 아직 방문하지 않은 경우
            if 0 <= nx < M and 0 <= ny < N and farm[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))


# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # M: 가로, N: 세로, K: 배추 위치의 개수
    M, N, K = map(int, input().split())

    # 배추밭 초기화 (0으로 초기화된 2D 배열)
    farm = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    # 배추 위치 입력
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    # 필요한 배추흰지렁이 마리 수 계산
    worm_count = 0

    for i in range(N):
        for j in range(M):
            # 배추가 있고 방문하지 않은 경우
            if farm[i][j] == 1 and not visited[i][j]:
                bfs(j, i, farm, visited, N, M)
                worm_count += 1

    # 결과 출력
    print(worm_count)