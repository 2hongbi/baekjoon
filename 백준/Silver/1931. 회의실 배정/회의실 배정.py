n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] >= end_time: # 이전 회의가 끝나는 시간 이후에 시작되는 시간 선택
        count += 1
        end_time = meetings[i][1]

print(count)