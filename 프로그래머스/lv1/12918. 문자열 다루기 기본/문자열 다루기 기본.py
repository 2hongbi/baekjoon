def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isnumeric():
            return True
        return False
    return False