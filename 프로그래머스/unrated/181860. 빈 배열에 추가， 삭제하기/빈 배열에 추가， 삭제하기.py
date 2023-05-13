def solution(arr, flag):
    answer = []
    for a, f in zip(arr, flag):
        if f:
            answer.extend([a for _ in range(a * 2)])
        else:
            for _ in range(a):
                answer.pop()
    return answer