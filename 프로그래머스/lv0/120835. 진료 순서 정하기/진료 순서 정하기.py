def solution(emergency):
    temp = emergency.copy()
    emergency.sort(reverse=True)
    priority = 1
    answer = [0] * len(emergency)
    
    for i in emergency:
        answer[temp.index(i)] = priority
        priority += 1
    return answer