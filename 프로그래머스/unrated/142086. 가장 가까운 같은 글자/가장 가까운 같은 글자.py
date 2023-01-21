from collections import defaultdict


def solution(s):
    answer = []
    alpha = defaultdict(str)
    for idx, i in enumerate(s):
        if i not in alpha.keys():
            answer.append(-1)
            alpha[i] = idx
        else:
            answer.append(idx - alpha[i])
            alpha[i] = idx
    return answer