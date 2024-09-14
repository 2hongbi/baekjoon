import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)
max_height = 0

while low <= high:
    mid = (low + high) // 2

    remain_trees = 0
    for t in trees:
        if t > mid:
            remain_trees += t - mid

    if remain_trees >= m:
        max_height = mid
        low = mid + 1
    else:
        high = mid - 1


print(max_height)