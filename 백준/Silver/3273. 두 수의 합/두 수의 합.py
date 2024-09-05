n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers.sort()

count = 0
start, end = 0, n - 1

while start < end:
    a, b = numbers[start], numbers[end]

    if x == a + b:
        start += 1
        end -= 1
        count += 1
    elif x < a + b:
        end -= 1
    else:
        start += 1

print(count)