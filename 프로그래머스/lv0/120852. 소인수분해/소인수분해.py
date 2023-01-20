def factorize(n):
    factor = 2
    factors = []
    
    while (factor**2 <= n):
        while n % factor == 0:
            n = n // factor
            factors.append(factor)
        factor += 1
    
    if n > 1:
        factors.append(n)
    factors = list(set(factors))
    factors.sort()
    return factors


def solution(n):
    return factorize(n)