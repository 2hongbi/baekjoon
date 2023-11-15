def is_prime(x):
    if x <= 1:
        return False
    
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    # 진수 변환
    k_base_num = ''
    while n > 0:
        k_base_num = str(n % k) + k_base_num
        n //= k

    potential_primes = k_base_num.split('0')
    
    answer = 0
    
    for num in potential_primes:
        if num and all(c != '0' for c in num) and is_prime(int(num)):
            answer += 1
            
    return answer