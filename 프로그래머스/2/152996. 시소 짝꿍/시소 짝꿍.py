# 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면, 시소 짝꿍
# 2, 3, 4 거리의 지점에 좌석이 하나씩 있음: 2:3, 2:4(1:2), 3:4 
from collections import defaultdict

def solution(weights):
    answer = 0
    
    weights_dict = defaultdict(int)
    for w in weights:
        weights_dict[w] += 1
        
    # 중복 조합 제거를 위한 세트
    unique_weights = sorted(weights_dict.keys())
    
    for i in range(len(unique_weights)):
        w1 = unique_weights[i]
        for j in range(i, len(unique_weights)):
            w2 = unique_weights[j]
            if w1 == w2:
                answer += weights_dict[w1] * (weights_dict[w1] - 1) // 2
            else:
                if w1 * 2 == w2 or w1 * 3 == w2 * 2 or w1 * 4 == w2 * 3:
                    answer += weights_dict[w1] * weights_dict[w2]
        
    
    
    return answer