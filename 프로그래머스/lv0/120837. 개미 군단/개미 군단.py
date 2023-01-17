def solution(hp):
    answer = 0
    power = 5
    while hp != 0:
        temp = hp // power
        answer += temp
        hp -= temp * power
        power -= 2
    return answer