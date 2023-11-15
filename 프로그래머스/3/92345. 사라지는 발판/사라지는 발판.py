def is_out_of_bounds(x, y, n, m):
    return x < 0 or x >= n or y < 0 or y >= m

def solve(board, curx, cury, opx, opy, vis):
    n, m = len(board), len(board[0])
    # 플레이어가 밟고 있는 발판이 사라졌다면
    if vis[curx][cury]: return 0
    ret = 0
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 상, 하, 좌, 우

    for dx, dy in directions:
        nx, ny = curx + dx, cury + dy
        if is_out_of_bounds(nx, ny, n, m) or vis[nx][ny] or board[nx][ny] == 0: continue
        vis[curx][cury] = 1

        val = solve(board, opx, opy, nx, ny, vis) + 1
        vis[curx][cury] = 0

        if ret % 2 == 0 and val % 2 == 1: 
            ret = val
        elif ret % 2 == 0 and val % 2 == 0: 
            ret = max(ret, val)
        elif ret % 2 == 1 and val % 2 == 1: 
            ret = min(ret, val)

    return ret

def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    vis = [[0] * m for _ in range(n)]
    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1], vis)