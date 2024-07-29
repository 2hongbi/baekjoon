# 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면, 시소 짝꿍
# 2, 3, 4 거리의 지점에 좌석이 하나씩 있음: 2:3, 2:4(1:2), 3:4 
from collections import defaultdict

def solution(weights):
    answer = 0
    
    weights_dict = defaultdict(int)
    for w in weights:
        weights_dict[w] += 1
        
        
    for w in weights_dict:
        # 동일한 무게 쌍
        if weights_dict[w] > 1:
            answer += weights_dict[w] * (weights_dict[w] - 1) // 2

        if w * 2 / 3 in weights_dict:
            answer += weights_dict[w] * weights_dict[w * 2 / 3]
        
        if w / 2 in weights_dict:
            answer += weights_dict[w] * weights_dict[w / 2]
        
        if w * 3 / 4 in weights_dict:
            answer += weights_dict[w] * weights_dict[w * 3 / 4]
    
    return answer