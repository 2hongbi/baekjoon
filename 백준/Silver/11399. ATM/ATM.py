n = int(input())
pi = list(map(int, input().split()))

pi.sort()

prev_time = pi[0]
total_time = pi[0]

for i in range(1, n):
    prev_time = pi[i] + prev_time
    total_time += prev_time

print(total_time)