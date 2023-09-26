def solution(elements):
    answer = []
    n = len(elements)
    elements *= 2
    
    for idx in range(1, n):
        for i in range(n):
            answer.append(sum(elements[i:i+idx]))
    
    return len(set(answer)) + 1