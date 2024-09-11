import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]


for i in range(n):
    print(numbers[i])