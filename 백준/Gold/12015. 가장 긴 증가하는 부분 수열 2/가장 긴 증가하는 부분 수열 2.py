import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = []

for num in arr:
    pos = bisect_left(lis, num) # 이분 탐색으로 현재 숫자가 들어갈 위치 찾기
    if pos == len(lis): # 현재 숫자가 lis의 모든 원소보다 크면 lis에 추가
        lis.append(num)
    else:
        lis[pos] = num


print(len(lis))