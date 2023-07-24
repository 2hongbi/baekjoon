def solution(sizes):
    # 시간 복잡도는 O(n)
    # width가 height보다 무조건 길다고 가정하자
    width = []
    height = []
    
    for x, y in sizes:
        if x < y:
            x, y = y, x
        
        width.append(x)
        height.append(y)
    
    return max(width) * max(height)
    