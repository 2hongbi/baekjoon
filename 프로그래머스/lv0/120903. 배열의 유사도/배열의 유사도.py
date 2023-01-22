def solution(s1, s2):
    intersection = set(s1) & set(s2)
    return len(intersection)