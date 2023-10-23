n, k = map(int, input().split())

coin_type = [int(input()) for _ in range(n)]

coin_type.sort(reverse=True)

cnt = 0
for coin in coin_type:
    cnt += k // coin
    k %= coin

print(cnt)