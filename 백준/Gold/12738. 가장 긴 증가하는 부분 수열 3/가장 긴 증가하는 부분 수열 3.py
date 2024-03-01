from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

lis = []

for num in arr:
    pos = bisect_left(lis, num)
    if pos == len(lis):
        lis.append(num)
    else: # 해당 위치의 값을 현재 숫자로 업데이트
        lis[pos] = num

print(len(lis))