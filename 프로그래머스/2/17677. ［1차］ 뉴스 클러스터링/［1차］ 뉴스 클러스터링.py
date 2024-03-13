def make_multiset(str):
    multiset = []
    for i in range(len(str)-1):
        elem = str[i:i+2].lower()
        if elem.isalpha():
            multiset.append(elem)
    return multiset


def calculate_jaccard(str1, str2):
    multiset1 = make_multiset(str1)
    multiset2 = make_multiset(str2)
    
    intersection = [] # 교집합
    union = multiset1.copy() # 합집합
    
    for elem in multiset2:
        if elem in multiset1:
            intersection.append(elem)
            multiset1.remove(elem)
        else:
            union.append(elem)
            
    if len(union) == 0:
        return 65536
    else:
        jaccard = len(intersection) / len(union)
        return int(jaccard * 65536)
    

def solution(str1, str2):
    answer = calculate_jaccard(str1, str2)
    return answer