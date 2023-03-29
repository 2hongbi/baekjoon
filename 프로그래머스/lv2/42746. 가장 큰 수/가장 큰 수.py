def solution(numbers):
    numbers = list(map(str, numbers))
    
    # x + y, y + x 비교 정렬
    # number은 1000이하의 숫자 -> x4 반복한 값으로 판단
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    else:
        return answer