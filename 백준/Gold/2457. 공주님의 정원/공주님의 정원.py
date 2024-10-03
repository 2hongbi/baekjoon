import sys
input = sys.stdin.readline

def to_date(month, day):
    # 날짜 mmdd
    return month * 100 + day

n = int(input())
flowers = []

for _ in range(n):
    start_month, start_day, end_month, end_day = map(int, input().split())
    start = to_date(start_month, start_day)
    end = to_date(end_month, end_day)
    flowers.append((start, end))

flowers.sort()

target_start = to_date(3, 1)
target_end = to_date(11, 30)

current_end = target_start
next_end = target_start
count, i = 0, 0

# 꽃이 피는 기간이 겹치는 부분을 최대한 활용
# 항상 가장 일찍 피고, 가장 늦게 지는 꽃을 선택하는 방식으로 진행
# 현재 선택한 꽃이 지는 날 이전에 피기 시작하는 꽃 중에서 가장 늦게 지는 꽃 선택해 나가기
while i < n and current_end <= target_end:
    found = False

    # 현재 범위를 넘는 꽃을 찾아서 멀리까지 커버하기
    while i < n and flowers[i][0] <= current_end:
        found = True
        next_end = max(next_end, flowers[i][1])
        i += 1

    if found:
        count += 1
        current_end = next_end
    else:
        break

# 11월 30일까지 덮지 못하면 0 출력
if current_end <= target_end:
    print(0)
else:
    print(count)