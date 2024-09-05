import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # k: 합을 구하기 위한 연속적인 날짜의 수
temperatures = list(map(int, input().split()))

current_temp = sum(temperatures[:k])
max_temp = current_temp

for i in range(k, n):
    current_temp += temperatures[i] - temperatures[i-k]
    if current_temp > max_temp:
        max_temp = current_temp

print(max_temp)