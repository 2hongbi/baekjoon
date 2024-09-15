n = int(input())
k = int(input())

def find_kth_number(n, k):
    low, high = 1, n * n

    while low <= high:
        mid = (low + high) // 2

        count = 0 # mid 이하 숫자가 몇 개인지 세기
        for i in range(1, n + 1):
            count += min(mid // i, n)

        if count < k:
            low = mid + 1
        else:
            high = mid - 1

    return low

print(find_kth_number(n, k))