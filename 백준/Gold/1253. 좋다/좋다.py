n = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

good_count = 0

for i in range(n):
    target = numbers[i]

    start, end = 0, n-1
    while start < end:
        # 자기 자신은 포함하면 안됨
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        total = numbers[start] + numbers[end]

        if total == target:
            good_count += 1
            break
        elif total < target:
            start += 1
        else:
            end -= 1


print(good_count)