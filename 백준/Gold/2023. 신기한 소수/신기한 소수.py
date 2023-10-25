import math
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def dfs(x):
    if len(str(x)) == n:
        print(x)
    else:
        for i in range(10):
            next_num = x * 10 + i
            if is_prime(next_num):
                dfs(next_num)

dfs(2)
dfs(3)
dfs(5)
dfs(7)