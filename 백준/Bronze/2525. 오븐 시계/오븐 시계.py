import sys
input = sys.stdin.readline

hour, minutes = map(int, input().split())
times = int(input())

minutes += times
if minutes >= 60:
    hour += minutes // 60
    minutes = minutes % 60

if hour >= 24:
    hour -= 24

print(hour, minutes)