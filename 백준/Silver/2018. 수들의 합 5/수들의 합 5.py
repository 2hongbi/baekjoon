import sys

input = sys.stdin.readline

n = int(input())

count = 1 # n 자기 자신만 있는 경우
current_sum = 1
start, end = 1, 1

while end != n:
    if current_sum == n:
        count += 1
        end += 1
        current_sum += end
    elif current_sum > n:
        current_sum -= start
        start += 1
    else:
        end += 1
        current_sum += end

print(count)