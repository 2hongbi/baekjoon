def solution(people, limit):
    answer = 0
    
    people.sort()
    left, right = 0, len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            right -= 1
            answer += 1 # 모든 사람을 구출하는 것이 목표이므로
    
    return answer