import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -float('inf')
min_value = float('inf')

def backtrack(idx, current_result, add, sub, mul, div):
    global max_value, min_value

    if idx == n:
        max_value = max(max_value, current_result)
        min_value = min(min_value, current_result)
        return

    if add > 0:
        backtrack(idx + 1, current_result + numbers[idx], add - 1, sub, mul, div)

    if sub > 0:
        backtrack(idx + 1, current_result - numbers[idx], add, sub - 1, mul, div)

    if mul > 0:
        backtrack(idx + 1, current_result * numbers[idx], add, sub, mul - 1, div)

    if div > 0:
        # 음수일 때 나눗셈 처리
        if current_result < 0:
            backtrack(idx + 1, -(-current_result // numbers[idx]), add, sub, mul, div - 1)
        else:
            backtrack(idx + 1, current_result // numbers[idx], add, sub, mul, div - 1)


backtrack(1, numbers[0], add, sub, mul, div)

print(max_value)
print(min_value)