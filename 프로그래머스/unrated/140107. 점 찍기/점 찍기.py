import math

def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k):
        answer += (d ** 2 - i ** 2) ** (1/2) // k + 1
    return answer