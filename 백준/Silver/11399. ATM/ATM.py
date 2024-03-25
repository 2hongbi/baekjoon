n = int(input())
pi = list(map(int, input().split()))

pi.sort()

ans, tmp = pi[0], pi[0]

for i in range(1, n):
    tmp += pi[i]
    ans += tmp

print(ans)