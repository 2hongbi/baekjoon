num = int(input())
scores = list(map(int, input().split()))
m = max(scores)

total = 0
for i in scores:
    total += (i / m) * 100

print(total / num)