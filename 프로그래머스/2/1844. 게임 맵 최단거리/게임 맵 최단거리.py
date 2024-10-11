from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
        
    return maps[-1][-1] if maps[-1][-1] != 1 else -1