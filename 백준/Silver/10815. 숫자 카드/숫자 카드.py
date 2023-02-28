import sys
input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().split()))
card_list.sort()
m = int(input())
check_list = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    temp = binary_search(card_list, check_list[i], 0, n-1)
    if temp is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')