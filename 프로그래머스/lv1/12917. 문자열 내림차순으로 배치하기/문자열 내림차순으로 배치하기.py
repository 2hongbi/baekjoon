def solution(s):
    temp = sorted([i for i in s if i.islower()], reverse=True) + sorted([i for i in s if i.isupper()], reverse=True)
    return ''.join(temp)
    