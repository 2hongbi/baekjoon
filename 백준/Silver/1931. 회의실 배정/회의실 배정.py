import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0])) # 종료 시각 기준으로 정렬하고, 종료 시각이 같으면 시작 시각 기준 정렬하기

count = 1
end_time = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] >= end_time: # 앞 회의의 종료 시각보다 시작 시각이 늦은 회의가 나온 경우
        count += 1
        end_time = meetings[i][1]

print(count)