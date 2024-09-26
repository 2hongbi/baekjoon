def hanoi(n, start, mid, end):
    if n == 1:
        print(f"{start} {end}")
    else:
        hanoi(n - 1, start, end, mid)
        print(f"{start} {end}")
        hanoi(n - 1, mid, start, end)

k = int(input())
print(2**k - 1)
hanoi(k, 1, 2, 3)