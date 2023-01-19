def solution(numbers, k):
    idx = 1
    for i in range(k - 1):
        idx += 2
        if idx > len(numbers) - 1:
            idx -= len(numbers)
    return idx