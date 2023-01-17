def solution(rsp):
    winning = {'0': '5', '2': '0', '5': '2'}
    answer = ''
    for i in rsp:
        answer += winning[i]
    return answer