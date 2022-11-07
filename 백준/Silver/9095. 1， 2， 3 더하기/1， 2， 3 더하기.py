def LRR(num):
    # Linear Recurrence Relations
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return LRR(num - 1) + LRR(num - 2) + LRR(num - 3)


T = int(input())
for _ in range(T):
    n = int(input())
    print(LRR(n))