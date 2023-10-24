n = int(input())

timeline = []
for _ in range(n):
    start, end = map(int, input().split())
    timeline.append([end, start]) # 종료 시각 우선 정렬이 먼저 -> 0번째에 종료 시각 먼저 작성

timeline.sort()

cnt = 0
end = -1

for i in range(n):
    if timeline[i][1] >= end: # 겹치지 않은 다음 회의
        end = timeline[i][0]
        cnt += 1

print(cnt)