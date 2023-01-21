def solution(s):
    for i in s:
        if s.count(i) > 1:
            s = s.replace(i, '')
    s = sorted(list(s))
    return ''.join(s)