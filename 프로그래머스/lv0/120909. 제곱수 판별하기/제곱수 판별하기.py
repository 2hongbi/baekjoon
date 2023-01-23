def solution(n):
    sqroot = int(n**(1/2))
    if sqroot**2 == n:
        return 1
    return 2