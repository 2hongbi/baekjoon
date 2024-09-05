import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

start = 0
current_sum = 0
min_length = n + 1 # 최소 길이 구간

# 투 포인터를 이용해서 부분합 계산하기
for end in range(n):
    current_sum += numbers[end]

    while current_sum >= s:
        min_length = min(min_length, end - start + 1) # 구간 길이 갱신
        current_sum -= numbers[start]
        start += 1

# 결과 출력
if min_length == n + 1:
    print(0)
else:
    print(min_length)