def solution(n, m, section):
    answer = 0
    last_painted = 0 # 마지막으로 칠한 구역의 끝 위치
    
    for s in section:
        if s > last_painted:
            answer += 1
            last_painted = s + m - 1
            
    return answer