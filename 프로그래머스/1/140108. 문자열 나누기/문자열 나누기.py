def solution(s):
    answer = 0
    index = 0
    
    while index < len(s):
        x = s[index]
        same, notsame = 0, 0
        
        for i in range(index, len(s)):
            if s[i] == x:
                same += 1
            else:
                notsame += 1
                
            if same == notsame:
                answer += 1
                index = i + 1
                break
        else:
            # 더 이상 분리할 수 없는 경우
            answer += 1
            break
        
    

    return answer