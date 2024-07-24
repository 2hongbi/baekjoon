# https://www.acmicpc.net/problem/1110
# 0보다 크거나 작고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있음
# 1. 주어진 수가 10보다 작다면, 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더함
# 2. 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있음
# ex. 26 = 2 + 6 = 8 -> 새로운 수는 68
# n이 주어졌을 때, n의 사이클의 길이를 구하자
import sys

n = int(sys.stdin.readline())

original_number = n
count = 0

while True:
    sum_digits = (n // 10) + (n % 10)
    new_digits = (n % 10) * 10 + (sum_digits % 10)

    count += 1

    if original_number == new_digits:
        break

    n = new_digits

print(count)