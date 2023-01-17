def solution(x):
    digit = sum(list(map(int, str(x))))
    if x % digit == 0:
        return True
    return False