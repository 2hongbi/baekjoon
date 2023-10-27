def solution(n):
    snail = [[0] * i for i in range(1, n + 1)]
    x, y = -1, 0
    number = 1
    
    for i in range(n):
        for j in range(i, n):
            angle = i % 3 
            if angle == 0:
                x += 1
            elif angle == 1:
                y += 1
            elif angle == 2:
                x -= 1
                y -= 1
            snail[x][y] = number
            number += 1
    
    result = []
    for row in snail:
        result.extend(row)
    return result
            