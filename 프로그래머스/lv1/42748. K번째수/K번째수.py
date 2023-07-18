def solution(array, commands):
    answer = []
    for cmd in commands:
        i, j, k = cmd[0], cmd[1], cmd[2]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer