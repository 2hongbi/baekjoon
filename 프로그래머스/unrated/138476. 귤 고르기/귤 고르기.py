from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    type = defaultdict(int)
    for t in tangerine:
        type[t] += 1
    
    sorted_type = sorted(type.items(), key=lambda item: item[1], reverse=True)
    
    for _, v in sorted_type:
        k -= v
        answer += 1
        if k <= 0:
            break
        
    return answer