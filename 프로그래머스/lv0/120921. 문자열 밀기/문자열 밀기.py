def solution(A, B):
    if A == B:
        return 0
    for i in range(1, len(A)+1):
        temp = A[-i:] + A[:len(A)-i]
        if temp == B:
            return i
    return -1