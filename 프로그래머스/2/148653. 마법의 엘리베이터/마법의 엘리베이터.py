# -1, +1 / -10, +10 / -100, +100 
# 엘리베이터가 위치해 있는 층과 버튼의 값을 더한 결과가 0보다 작으면
# 엘리베이터는 움직이지 않음
# 항상 최소한의 버튼을 눌러서 이동하기 >> greedy 기법인가?
# 16: 해당 자리가 5보다 크니까 그냥 올려주기
# 2554: 해당 자리가 5보다 작으면 그냥 내리고..
def solution(storey):
    answer = 0
    
    while storey > 0:
        current_digit = storey % 10 # 현재 자리의 숫자
        
        if current_digit > 5:
            answer += (10 - current_digit)
            storey += 10
        elif current_digit < 5:
            answer += current_digit
        else:
            # 5인 경우는 그 다음 자리 숫자에 따라 결정하기
            next_digit = (storey // 10) % 10
            answer += 5
            if next_digit >= 5:
                storey += 10 # 다음 자리로 올리기
        
        # 처리된 자리 없애기
        storey //= 10
                
    return answer