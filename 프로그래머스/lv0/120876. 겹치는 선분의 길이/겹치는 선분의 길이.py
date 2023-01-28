def solution(lines):
    arr = [0 for i in range(201)]
    ans = 0
    for line in lines:
        for i in range(line[0], line[1]):
            arr[i] += 1
    for a in arr:
        if a > 1:
            ans += 1
    return ans
        
        