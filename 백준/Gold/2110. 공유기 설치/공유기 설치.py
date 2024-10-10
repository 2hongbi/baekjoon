import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]

houses.sort()

start = 1
end = houses[-1] - houses[0] # 공유기 최대 거리
answer = 0

while start <= end:
    mid = (start + end) // 2
    current = houses[0]
    count = 1

    # 공유기 체크
    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            count += 1
            current = houses[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)