def solution(num, k):
    num = list(map(int, str(num)))
    for i in range(len(num)):
        if num[i] == k:
            return i + 1
    return -1