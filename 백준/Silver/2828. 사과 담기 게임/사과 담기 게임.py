n, m = map(int, input().split())
j = int(input())
apples = [int(input()) for _ in range(j)]

# 바구니 초기 위치 설정
left, right = 1, m
answer = 0

for apple in apples:
    if apple < left:
        answer += left - apple
        left = apple
        right = left + m - 1
    elif apple > right:
        answer += apple - right
        right = apple
        left = right - m + 1

print(answer)