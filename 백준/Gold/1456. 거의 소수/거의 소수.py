import math

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(2, limit + 1) if sieve[i]]


def count_almost_primes(a, b):
    sqrt_b = int(math.sqrt(b)) # b의 제곱근까지만 소수를 구함
    primes = sieve_of_eratosthenes(sqrt_b)

    count = 0

    for prime in primes:
        power = prime * prime
        while power <= b:
            if power >= a:
                count += 1
            if power > b // prime: # overflow qkdwl
                break
            power *= prime
    return count

a, b = map(int, input().split())
print(count_almost_primes(a, b))