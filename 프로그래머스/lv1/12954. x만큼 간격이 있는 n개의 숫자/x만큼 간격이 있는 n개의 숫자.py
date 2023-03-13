def solution(x, n):
    if x == 0:
        return [0] * n
    answer = [i for i in range(x, x*n+x, x)]
    return answer