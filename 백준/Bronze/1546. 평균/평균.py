num = int(input())
scores = list(map(int, input().split()))
m = max(scores)
s = sum(scores)

print(s * 100 / m / num)