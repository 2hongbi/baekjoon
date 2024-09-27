from collections import deque

# 입력 받기
R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

# 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 불과 지훈이의 BFS 큐
fire_queue = deque()
jihun_queue = deque()

# 불과 지훈이의 방문 시간
fire_time = [[-1] * C for _ in range(R)]
jihun_time = [[-1] * C for _ in range(R)]

# 초기 설정
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            fire_queue.append((i, j))
            fire_time[i][j] = 0
        if maze[i][j] == 'J':
            jihun_queue.append((i, j))
            jihun_time[i][j] = 0

# 불의 BFS
while fire_queue:
    x, y = fire_queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if maze[nx][ny] != '#' and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_queue.append((nx, ny))

# 지훈이의 BFS
while jihun_queue:
    x, y = jihun_queue.popleft()

    # 가장자리인지 확인하여 탈출 가능한지 체크
    if x == 0 or x == R - 1 or y == 0 or y == C - 1:
        print(jihun_time[x][y] + 1)
        exit()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if maze[nx][ny] == '.' and jihun_time[nx][ny] == -1:
                # 불이 아직 도착하지 않았거나, 불보다 먼저 도착할 수 있는 경우
                if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                    jihun_time[nx][ny] = jihun_time[x][y] + 1
                    jihun_queue.append((nx, ny))

# 탈출할 수 없는 경우
print("IMPOSSIBLE")