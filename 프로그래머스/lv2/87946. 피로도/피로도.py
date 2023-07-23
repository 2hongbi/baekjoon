from collections import deque

def solution(k, dungeons):
    dp = deque()
    n = 0
    dp.append([k, []]) # 현재 남은 체력이 k고, 현재 [] 방문함
    
    while dp:
        p, v = dp.popleft() # 피로도, 던전
        for i in range(len(dungeons)):
            [a, b] = dungeons[i]
            
            if i not in v and p >= a and p - b >= 1:
                dp.append([p - b, v + [i]])
            else:
                n = max(n, len(v))
    return n