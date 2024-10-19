import sys
input = sys.stdin.readline

n, m = map(int, input().split())
amounts = [int(input()) for _ in range(n)]

def is_possible(k, n, m, amounts):
    count = 1
    current_sum = 0

    for amount in amounts:
        if current_sum + amount > k:
            count += 1
            current_sum = amount
            if count > m:
                return False
        else:
            current_sum += amount
    return True


# k가 너무 적으면 하루를 못 버팀
# 인출금액 k가 너무 크면 인출 횟수는 적음
def find_minimum(n, m, amounts):
    low = max(amounts)
    high = sum(amounts)

    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid, n, m, amounts):
            high = mid - 1
        else:
            low = mid + 1
    return low

result = find_minimum(n, m, amounts)
print(result)