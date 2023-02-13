import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ingredients = list(map(int, input().split()))

ingredients.sort()

i, j = 0, n - 1
ans = 0

while i < j:
    if ingredients[i] + ingredients[j] < m:
        i += 1
    elif ingredients[i] + ingredients[j] > m:
        j -= 1
    else:
        ans += 1
        i += 1
        j -= 1

print(ans)