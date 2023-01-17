def get_divisor(n):
    divisor_list = []

    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            divisor_list.append(i)
            if (i**2) != n:
                divisor_list.append(n // i)
    divisor_list.sort()
    return divisor_list


def solution(n):
    divisor_list = get_divisor(n)
    return sum(divisor_list)