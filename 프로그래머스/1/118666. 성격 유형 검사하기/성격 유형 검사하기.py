from collections import defaultdict

def solution(survey, choices):
    type_dict = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')] # 처음에는 {}로 dict 처리 했는데, 순서 보장 안하는걸 까먹음...
    personality = defaultdict(int)
    for s, c in zip(survey, choices):
        # print(s, c)
        if c < 4:
            personality[s[0]] += (4 - c)
        elif c > 4:
            personality[s[1]] += (c - 4)
            
    answer = ''
    for t in type_dict:
        print(t)
        if personality[t[0]] >= personality[t[1]]:
            answer += t[0]
        else:
            answer += t[1]
    
    return answer