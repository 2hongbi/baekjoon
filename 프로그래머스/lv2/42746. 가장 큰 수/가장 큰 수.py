def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    
    
    # 테케 11번 아마 0이 원소인 경우임 -> 000이 아닌 0 리턴하도록
    if numbers[0] == '0':
        return '0'
    
    return ''.join(numbers)