def solution(board, skill):
    n, m = len(board), len(board[0])
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    
    for t, r1, c1, r2, c2, degree in skill:
        degree = degree if t == 2 else -degree
        visited[r1][c1] += degree
        visited[r1][c2 + 1] -= degree
        visited[r2 + 1][c1] -= degree
        visited[r2 + 1][c2 + 1] += degree
    
    # 가로 방향 누적합
    for i in range(n):
        for j in range(1, m):
            visited[i][j] += visited[i][j - 1]

    # 세로 방향 누적합
    for j in range(m):
        for i in range(1, n):
            visited[i][j] += visited[i - 1][j]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + visited[i][j] > 0:
                answer += 1
            
    return answer
