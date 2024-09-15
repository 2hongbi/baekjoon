import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

numbers.sort()

def binary_search(arr, x):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    else:
        return False

for t in targets:
    print(1) if binary_search(numbers, t) else print(0)