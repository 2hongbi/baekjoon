n = int(input())
x = list(map(int, input().split()))

total_sum = sum(x)
result = 0

for i in range(n):
    total_sum -= x[i]
    result += total_sum * x[i]

print(result)