import sys

input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())


def find_max_budgets(budgets, total_budget):
    # 이분 탐색
    low, high = 0, max(budgets)
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        allocated = 0

        for budget in budgets:
            if budget > mid:
                allocated += mid
            else:
                allocated += budget

        if allocated <= total_budget:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer


print(find_max_budgets(budgets, total_budget))