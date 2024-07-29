n = int(input())
nums = list(map(int, input().split()))

# 카데인 알고리즘 이용
max_sum, current_sum = nums[0], nums[0]

for i in range(1, n):
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)