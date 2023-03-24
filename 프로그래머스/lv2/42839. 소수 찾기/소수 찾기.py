import math
from itertools import combinations, permutations


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    
    permu = []
    for i in range(1, len(numbers) + 1):
        permu.extend(list(permutations(list(numbers), i)))
        
    permu = list(set(permu))
    ans = []
    for p in permu:
        temp = int(''.join(p))
        if temp > 1 and is_prime_number(temp):
            ans.append(temp)
            
    return len(set(ans))