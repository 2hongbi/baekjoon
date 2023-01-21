def is_sosu(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
            

def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                total = nums[i] + nums[j] + nums[k]

                if is_sosu(total):
                    answer += 1
    return answer