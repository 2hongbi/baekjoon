from collections import defaultdict


def solution(numlist, n):
    answer = []
    dict = defaultdict(list)
    for num in numlist:
        i = abs(num - n)
        dict[i].append(num)
    
    for key, value in sorted(dict.items()):
        if len(value) > 1:
            value.sort(reverse=True)
        answer.extend(value)
    
    return answer