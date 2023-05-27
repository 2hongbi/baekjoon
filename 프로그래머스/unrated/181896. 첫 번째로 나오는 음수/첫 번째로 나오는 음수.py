def solution(num_list):
    for idx, n in enumerate(num_list):
        if n < 0:
            return idx 
    return -1