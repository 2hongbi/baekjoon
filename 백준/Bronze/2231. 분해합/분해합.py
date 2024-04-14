N = int(input())

ans = 0

for i in range(1, N):
    total = sum(map(int, str(i)))
    total += i

    if total == N:
        ans = i
        break

print(ans)