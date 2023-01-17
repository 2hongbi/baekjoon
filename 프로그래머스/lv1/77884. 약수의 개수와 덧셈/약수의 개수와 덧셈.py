def get_divisor(n):
    divisor_list = []
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            divisor_list.append(i)
            if (i**2) != n:
                divisor_list.append(n//i)
    divisor_list.sort()
    return divisor_list


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if len(get_divisor(i)) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer