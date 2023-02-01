from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)
    for c in clothes:
        clothes_dict[c[1]].append(c[0])
    
    answer = 1
    for k, v in clothes_dict.items():
        answer *= len(v) + 1
    return answer - 1