def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        tmp = 0
        for nm in p:
            if nm in name:
                tmp += yearning[name.index(nm)]
        answer.append(tmp)
    return answer