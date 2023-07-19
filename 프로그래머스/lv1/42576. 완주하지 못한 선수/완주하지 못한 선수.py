from collections import Counter # 데이터 셀 때 유용

# dictionary가 list보다 최소 수십 배 이상 빠름
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]