import string

def solution(s, skip, index):
    answer = ''
    
    alpha = string.ascii_lowercase
    
    for ch in skip:
        if ch in alpha:
            alpha = alpha.replace(ch, '')
    
    for i in s:
        tmp = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += tmp
    
    return answer