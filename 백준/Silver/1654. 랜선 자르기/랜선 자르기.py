import sys

input = sys.stdin.readline

k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

max_length = 0

low, high = 1, max(cables)  # 랜선 길이는 1부터 가능

while low <= high:
    mid = (low + high) // 2

    temp = sum(cable // mid for cable in cables)

    if temp >= n: # 충분한 길이로 잘라졌다면, 더 긴 길이로 시도
        max_length = mid
        low = mid + 1
    else:
        high = mid - 1


print(max_length)