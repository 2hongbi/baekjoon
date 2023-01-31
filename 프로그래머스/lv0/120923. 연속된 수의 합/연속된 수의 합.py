def solution(num, total):
    idx = total // num    
    return [i for i in range(idx - (num-1) // 2, idx + (num+2)//2)]