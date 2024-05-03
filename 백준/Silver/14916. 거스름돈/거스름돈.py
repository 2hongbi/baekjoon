n = int(input())

def min_coins(n):
    five_count = n // 5

    for i in range(five_count, -1, -1):
        remaining = n - (i * 5)
        if remaining % 2 == 0:
            return i + remaining // 2

    return -1

print(min_coins(n))