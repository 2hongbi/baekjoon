def in_range(x, y, z):
    return 0 <= x < z and 0 <= y < z

def solution(board, h, w):
    z = len(board)

    target = board[h][w]
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    answer = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = h + dx, w + dy
        if in_range(nx, ny, z) and board[nx][ny] == target:            
            answer += 1
    return answer