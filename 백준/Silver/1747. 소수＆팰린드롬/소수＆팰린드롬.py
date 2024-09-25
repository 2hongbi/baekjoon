import math


# 소수 판별
def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# 팰린드롬 판별
def is_palindrome(x):
    return str(x) == str(x)[::-1]


n = int(input())

while True:
    if is_palindrome(n) and is_prime(n):
        print(n)
        break
    n += 1