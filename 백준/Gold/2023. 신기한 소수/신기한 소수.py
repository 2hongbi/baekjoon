import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

def is_prime(x):
    # 소수 판별 함수
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def dfs(number):
    if len(str(number)) == n:
        print(number)
        return

    for digit in range(1, 10, 2):
        new_number = number * 10 + digit
        if is_prime(new_number):
            dfs(new_number)


for i in [2, 3, 5, 7]:
    dfs(i)