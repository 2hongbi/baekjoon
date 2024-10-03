import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    max_profit = 0
    max_price = 0

    for i in range(n - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            max_profit += max_price - prices[i]

    print(max_profit)