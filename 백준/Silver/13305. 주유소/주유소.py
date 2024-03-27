n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

current_price = prices[0]
total_cost = 0

for i in range(n - 1):
    if prices[i] < current_price:
        current_price = prices[i]
    total_cost += current_price * distances[i]

print(total_cost)