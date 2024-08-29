def solution(gems):
    gem_types = len(set(gems))
    gem_dict = {}
    left = 0
    min_length = len(gems) + 1 # 최소 구간 길이
    answer = [0, len(gems) - 1]
    
    for right in range(len(gems)):
        # 오른쪽 포인터가 가리키는 보석 추가
        if gems[right] in gem_dict:
            gem_dict[gems[right]] += 1
        else:
            gem_dict[gems[right]] = 1
        
        while len(gem_dict) == gem_types:
            if right - left < min_length:
                min_length = right - left
                answer = [left + 1, right + 1]

            # 구간 좁히기
            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]
            left += 1
    
    return answer