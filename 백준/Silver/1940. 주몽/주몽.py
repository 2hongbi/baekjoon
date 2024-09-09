n = int(input())
m = int(input())

ingredients = list(map(int, input().split()))
ingredients.sort()

start, end = 0, n-1
count = 0

while start < end:
    guard = ingredients[start] + ingredients[end]
    if guard == m:
        count += 1
        start += 1
        end -= 1
    elif guard < m:
        start += 1
    else:
        end -= 1

print(count)