import sys
input = sys.stdin.readline

# 양수, 음수, 1, 0 구분해서 리스트 저장
# 각각의 리스트 정렬 > 양수는 내림차순 -> 큰 수끼리 묶기, 음수는 오름차순 정렬 -> 절댓값이 큰 수끼리
# 1보다 큰 양수는 가능한 한 곱하고, 음수는 곱할 수 있을 만큼 묶기

n = int(input())
numbers = [int(input()) for _ in range(n)]

positive, negative = [], []
zeros, ones = 0, 0

result = 0

for num in numbers:
    if num > 1:
        positive.append(num)
    elif num == 0:
        zeros += 1
    elif num == 1:
        ones += 1
    else:
        negative.append(num)

positive.sort(reverse=True) # 내림차순 정렬
negative.sort()

# 양수 두 개씩 묶어 곱하기
for i in range(0, len(positive) - 1, 2):
    result += positive[i] * positive[i + 1]
# 남은 양수가 있으면 더하기
if len(positive) % 2 == 1:
    result += positive[-1]

# 음수 두 개씩 묶어 곱하기
for i in range(0, len(negative) - 1, 2):
    result += negative[i] * negative[i + 1]
# 음수가 홀수 개 남았을 때 0이 있으면 묶어서 없애기
if len(negative) % 2 == 1 and zeros == 0:
    result += negative[-1]

# 1은 더하기
result += ones

print(result)