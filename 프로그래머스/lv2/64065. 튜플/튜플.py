def solution(s):
    result = []
    ls = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)
    for l in ls:
        for ll in l:
            if int(ll) not in result:
                result.append(int(ll))
                break
    return result