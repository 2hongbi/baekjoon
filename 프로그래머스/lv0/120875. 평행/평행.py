def solution(dots):
    answer = []
    for i in range(len(dots) - 1):
        for j in range(i + 1, len(dots)):
            x = dots[j][0] - dots[i][0]
            y = dots[j][1] - dots[i][1]
            answer.append(x/y)
    return 1 if len(answer) != len(set(answer)) else 0 