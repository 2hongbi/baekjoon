def solution(s):
    ans = len(s) // 2
    if len(s) % 2 == 0:
        return s[ans-1:ans+1]
    else:
        return s[ans]