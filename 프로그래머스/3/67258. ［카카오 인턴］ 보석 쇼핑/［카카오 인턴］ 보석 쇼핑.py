def solution(gems):
    gem_types = len(set(gems))  # 보석 종류의 수
    gem_dict = {}
    left = 0  # 왼쪽 포인터
    min_length = len(gems) + 1  # 최소 구간 길이
    answer = [0, len(gems) - 1]  # 최소 구간의 시작과 끝 인덱스
    
    for right in range(len(gems)):
        # 오른쪽 포인터가 가리키는 보석을 추가
        if gems[right] in gem_dict:
            gem_dict[gems[right]] += 1
        else:
            gem_dict[gems[right]] = 1
        
        # 모든 보석을 포함하는 구간인지 확인
        while len(gem_dict) == gem_types:
            # 현재 구간이 최소 구간인지 확인
            if right - left < min_length:
                min_length = right - left
                answer = [left + 1, right + 1] 
            
            # 왼쪽 포인터를 이동시켜 구간을 좁힘
            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]
            left += 1
    
    return answer