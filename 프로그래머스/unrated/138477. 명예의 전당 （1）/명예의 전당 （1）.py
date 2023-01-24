def solution(k, score):
    answer = []
    temp = []
    for i in score:
        temp.append(i)
        temp.sort(reverse=True)
        if len(temp) > k:
            del temp[-1]
        answer.append(temp[-1])
    return answer