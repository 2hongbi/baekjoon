def get_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

def solution(balls, share):
    return get_factorial(balls) // (get_factorial(balls - share) * get_factorial(share))