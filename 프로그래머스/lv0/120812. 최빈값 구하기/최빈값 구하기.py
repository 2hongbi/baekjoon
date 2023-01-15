def solution(array):
    count = list(set(array))
    ans = [array.count(c) for c in count]
    
    if ans.count(max(ans)) == 1:
        idx = ans.index(max(ans))
        return count[idx]
    else:
        return -1
    