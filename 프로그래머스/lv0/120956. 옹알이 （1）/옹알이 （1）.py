def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        if any(p in bab for p in pron):
            for p in pron:
                bab = bab.replace(p, " ")
        
        if not bab.strip():
            answer += 1
            
    return answer