import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
idx = 0

for i in range(n - 1, 0, -1):
    if nums[i - 1] < nums[i]:
        idx = i - 1
        break

for i in range(n - 1, 0, -1):
    if nums[idx] < nums[i]:
        nums[idx], nums[i] = nums[i], nums[idx]
        nums = nums[:idx + 1] + sorted(nums[idx + 1:])
        print(*nums)
        exit()
print(-1)