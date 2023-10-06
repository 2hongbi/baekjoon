from itertools import combinations


def solution(numbers):
    answer = set()
    comb = list(combinations(numbers, 2))
    for c in comb:
        (a, b) = c
        answer.add(a + b)
    
    return sorted(answer)