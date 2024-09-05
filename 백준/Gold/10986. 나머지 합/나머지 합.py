import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 누적합과 나머지 계산하기
prefix = [0] * (n + 1)
mod_count = [0] * m  # 나머지 값의 개수 저장
mod_count[0] = 1 # 0번째 누적합이 m으로 떨어지는 경우 고려

current_sum = 0
result = 0

# 각 누적합 prefix[i]에 대해서 prefix[i] % m을 계산해서 그 값을 mod_count에 저장하기
# 만약 prefix[i] % m == 0 이라면, 이 자체로 구간 [0, i]는 m으로 나누어 떨어지는 구간임
for i in range(1, n + 1):
    current_sum += numbers[i - 1]
    remainder = current_sum % m

    # 나머지가 같은 구간의 수만큼 추가
    result += mod_count[remainder]
    mod_count[remainder] += 1

print(result)