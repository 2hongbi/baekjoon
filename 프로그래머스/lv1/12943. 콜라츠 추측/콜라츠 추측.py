def collatz(n, answer):
    if n == 1:
        return answer
    if answer == 500:
        return -1
    
    if n % 2 == 0:
        return collatz(n // 2, answer + 1)
    else:
        return collatz(n * 3 + 1, answer + 1)


def solution(num):
    return collatz(num, 0)