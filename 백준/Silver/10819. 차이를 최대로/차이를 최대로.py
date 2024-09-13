from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

def calculate_expression_value(arr):
    value = 0
    for i in range(n - 1):
        value += abs(arr[i] - arr[i + 1])
    return value


def max_expression_value(n, array):
    max_value = 0

    for perm in permutations(array):
        value = calculate_expression_value(perm)
        max_value = max(max_value, value)

    return max_value

print(max_expression_value(n, numbers))