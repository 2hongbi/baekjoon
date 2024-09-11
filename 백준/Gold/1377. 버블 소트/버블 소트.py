import sys
input = sys.stdin.readline

n = int(input())
arr = [(int(input()), idx) for idx in range(n)]

ans = 0
sorted_arr = sorted(arr)

for i in range(n):
    if ans < sorted_arr[i][1] - i:
        ans = sorted_arr[i][1] - i

print(ans + 1)