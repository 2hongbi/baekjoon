def solution(num_list):
    answer = ['', '']
    for n in num_list:
        if n % 2 == 0:
            answer[0] += str(n)
        else:
            answer[1] += str(n)
    
    return sum(map(int, answer))