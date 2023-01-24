def solution(k, m, score):
    if len(score) < m:
        return 0
    price = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if len(score[i:i+m]) < m:
            break
        price += min(score[i:i+m]) * m
    return price