def solution(arr):
    stack = []
    
    for a in arr:
        # 리스트 슬라이싱을 사용하면 비어있는 리스트에 대해서도 오류 없이 비교할 수 있음
        if stack[-1:] == [a]:
            continue
        stack.append(a)
    
    return stack