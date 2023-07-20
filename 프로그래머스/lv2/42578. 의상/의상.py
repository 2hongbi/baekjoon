def solution(clothes):
    clothes_dict = {}
    
    for c, kind in clothes:
        clothes_dict[kind] = clothes_dict.get(kind, 0) + 1
    
    answer = 1
    for c in clothes_dict.values():
        answer *= c + 1
    
    return answer - 1