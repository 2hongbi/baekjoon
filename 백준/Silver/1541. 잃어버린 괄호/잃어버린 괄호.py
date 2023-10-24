nums = list(map(str, input().split('-')))

def calculate_sum(n):
    result = 0
    temp = str(n).split('+')
    for t in temp:
        result += int(t)
    return result

answer = 0
for i in range(len(nums)):
    if i == 0:
        answer += calculate_sum(nums[i])
    else:
        answer -= calculate_sum(nums[i])

print(answer)