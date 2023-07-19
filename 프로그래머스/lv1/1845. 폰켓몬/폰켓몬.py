def solution(nums):
    num = len(nums) // 2
    kind = set(nums)
    
    if len(kind) > num:
        return num
    else:
        return len(kind)